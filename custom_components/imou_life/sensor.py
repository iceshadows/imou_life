"""Sensor platform for Imou."""
from collections.abc import Callable
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .entity import ImouEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)


# async def async_setup_entry(hass, entry, async_add_devices):
async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_devices: Callable
):
    """Configure platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    device = coordinator.device
    sensors = []
    for sensor_instance in coordinator.device.get_sensors_by_platform("sensor"):
        sensor = ImouSensor(coordinator, entry, sensor_instance)
        sensors.append(sensor)
        _LOGGER.debug(
            "[%s] Adding %s", device.get_name(), sensor_instance.get_description()
        )
    async_add_devices(sensors)


class ImouSensor(ImouEntity):
    """imou sensor class."""

    @property
    def device_class(self) -> str:
        """Device device class."""
        return self.sensor_instance.get_device_class()

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.sensor_instance.get_state()
