#
#      Open Source SAM-BA Programmer
#      Released under the MIT license
#
#   dean [at] fourwalledcubicle [dot] com
#         www.fourwalledcubicle.com
#

from . import Part
from .CortexM7 import CortexM7
from ..FlashControllers import EEFCFlash, AddressRange
from ..Peripheral import RSTC


class SAMV7(CortexM7):
	"""Base part class for SAMV7 series."""


	def __init__(self, samba, flash_planes, flash_total_length):
		"""Initializes class with flash & RSTC

		Args:
			flash_planes       -- flash planes & controllers count: 1 or 2
			flash_total_length -- total flash length, kBytes
		"""
		CortexM7.__init__(self, samba)
		self.flash_address_range = AddressRange(0x00400000, flash_total_length * 1024, int((flash_total_length * 1024) // flash_planes))
		if flash_planes == 1:
			self.flash_controllers = (
				EEFCFlash.Flash(self.samba, 0x00400000, 0x400E0C00, flash_total_length * 2, 512, dont_use_read_block=True),
            )
		else:
			# Unimplemented
			exit(0)
		self.reset_controller = RSTC(samba, 0x400E1800)


	@classmethod
	def identify(cls, ids):
		if not hasattr(cls, 'CHIP_ID'):
			return False
		try:
			chip_id = ids['CHIPID'].chip_id & 0x7FFFFFE0 # remove revision (A, B)
		except:
			return False
		return chip_id == cls.CHIP_ID


	@classmethod
	def get_name(cls):
		"""Retrieves the part name as a string. This extracts out the actual
		   class name of the sub-classed parts.

		Returns:
			Name of the SAM part, as a string (empty string for base classes).
		"""
		return '' if cls is SAMV7 else cls.__name__


@Part.UntestedPart
class ATSAMV7Q21B(SAMV7):
	CHIP_ID = 0x21220E00
	def __init__(self, samba):
		SAMV7.__init__(self, samba, 1, 2 * 1024)

