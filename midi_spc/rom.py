from __future__ import print_function, unicode_literals, division, absolute_import
import six
u = six.u

class Mapper (object):
    _image = None

    def __init__ (self, filename=None, fp=None, image=None):
        if image:
            self._image = image
        else:
            if filename and not fp:
                fp = open(filename, 'r+b')
            elif not fp:
                raise ValueError(u("One of filename or fp MUST be provided to Mapper"));
            self._image = fp.read()

    def _offset (self, snes_addr, intent=1):
        """Convert a SNES address to an image file offset.

        Default implementation is a NOP."""

        return snes_addr

    def _address (self, file_offset):
        """Convert an image file offset to SNES address (invert _offset())."""

        return file_offset

    def _to_word (self, seq2):
        """Convert a 2-byte sequence to an integer value.
        
        Default implementation suitable for little-endian images."""

        return seq2[0] | (seq2[1] << 8)

    def _from_word (self, word):
        """Convert an integer value to a 2-byte sequence.
        
        Default implementation suitable for little-endian images."""

        b = bytes(2)
        b[0] = word & 0xFF
        b[1] = (word & 0xFF00) >> 8
        return b

    def getb (self, addr):
        """Read a byte from the image at SNES address addr."""

        return self._image[self._offset(addr)]

    def getw (self, addr, signed=False):
        """Read a word as integer from the image at SNES address addr."""

        faddr = self._offset(addr, 2)
        val = self._to_word(self._image[faddr:faddr+2])
        if signed and (val & 0x8000) > 0:
            val = -(1 + val)
        return val

    def getvec (self, addr, n):
        """Read n bytes as a sequence from the image at SNES address addr."""

        faddr = self._offset(addr, n)
        return self._image[faddr:faddr+n]

    def putb (self, addr, val):
        """Write a byte value of val to the image at SNES address addr."""

        self._image[self._offset(addr)] = val & 0xFF

    def putw (self, addr, val):
        """Write a word value of val to the image at SNES address addr."""

        faddr = self._offset(addr, 2)
        self._image[faddr:faddr+2] = self._from_word(val & 0xFFFF)

    def putvec (self, addr, vec):
        """Write a sequence of bytes in vec to the image at SNES address addr."""

        n = len(vec)
        faddr = self._offset(addr, n)
        self._image[faddr:faddr+n] = vec


class LoRom (Mapper):
    _banks = None # number of 32K banks in the cart

    def __init__ (self, cart_size=64, **kwargs):
        Mapper.__init__(self, **kwargs)
        self._banks = cart_size

    def _offset (self, snes_addr, intent=1):
        bank = (snes_addr & 0xFF0000) >> 16
        if bank > self._banks:
            raise ValueError(u("Bank {0:X} exceeds max bank ID {1:X}").format(bank, self._banks - 1))

        # FIXME: this should work for Super Metroid on banks $80-$DF.  Need to find out
        # the proper LoRom mapping and make sure this is 100% legit.
        bank_addr = snes_addr & 0x7FFF
        if 0 > bank_addr or (bank_addr + intent) > 0x8000:
            msg = u("Access to {0:X} bytes in LoROM {1:X} exceeds bank (started at {2:X})")
            raise ValueError(msg.format(intent, snes_addr, bank_addr))

        return bank_addr | ((snes_addr & 0x7F0000) >> 1)


class SpcRam (Mapper):
    def _offset (self, snes_addr, intent=1):
        if 0 <= snes_addr <= (0x10000 - intent):
            return snes_addr + 0x100
        msg = u("Can't access {0:X} bytes at SPC offset {1:X}")
        raise ValueError(msg.format(intent, snes_addr))

