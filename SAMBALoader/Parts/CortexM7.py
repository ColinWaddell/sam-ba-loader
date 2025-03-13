
from .CortexM3_4 import CortexM3_4


class CortexM7(CortexM3_4):
	"""Common part implementation for the Cortex M7 family devices.

	It's expected to inheritors to set the variables:
	self.flash_address_range as AddressRange -- entire flash address region
	self.flash_controllers as list of FlashControllerBase -- flash planes with each own controller
	self.reset_controller as RSTC -- reset controller (optional)
	"""

	pass