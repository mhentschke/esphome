#pragma once

#ifdef USE_RP2040

#include <Arduino.h>
#include "esphome/core/hal.h"

namespace esphome {
namespace rp2040 {

class RP2040GPIOPin : public InternalGPIOPin {
 public:
  void set_pin(uint8_t pin) { pin_ = pin; }
  void set_inverted(bool inverted) { inverted_ = inverted; }
  void set_flags(gpio::Flags flags) { flags_ = flags; }

  void setup() override { pin_mode(flags_); }
  void pin_mode(gpio::Flags flags) override;
  bool digital_read() override;
  void digital_write(bool value) override;
  std::string dump_summary() const override;
  void detach_interrupt() const override;
  ISRInternalGPIOPin to_isr() const override;
  uint8_t get_pin() const override { return pin_; }
  gpio::Flags get_flags() const override { return flags_; }
  bool is_inverted() const override { return inverted_; }

 protected:
  void attach_interrupt(void (*func)(void *), void *arg, gpio::InterruptType type) const override;

  uint8_t pin_;
  bool inverted_;
  gpio::Flags flags_;
};

}  // namespace rp2040
}  // namespace esphome

#endif  // USE_RP2040
