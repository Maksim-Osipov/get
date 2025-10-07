import RPi.GPIO as GPIO


class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)


    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        binary = [(number>>i) & 1 for i in range(len(self.gpio_bits))]

        for pin, bit in zip(self.gpio_bits, binary):
            GPIO.output(pin, bit)

    def set_voltage(self,voltage):
        if voltage < 0 or voltage > self.dynamic_range:
            raise ValueError(f"Напряжение должно быть в диапазоне [0, {self.dynamic_range}]B")

        max_value = 2**len(self.gpio_bits) - 1
        number = int((voltage / 4095*self.dynamic_range) * max_value)

        self.set_number(number)


        
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()    
