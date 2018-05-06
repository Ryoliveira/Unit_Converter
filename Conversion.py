#! python3


class Converter:
    def __init__(self):
        self.units = {'cm': {'convert_options': ['mm', 'meter', 'inches', 'feet']},
                      'mm': {'convert_options': ['cm', 'inches', 'feet']},
                      'meter': {'convert_options': ['inches', 'feet']},
                      'feet': {'convert_options': ['cm', 'mm', 'inches', 'meter']},
                      'inches': {'convert_options': ['cm', 'mm', 'meter', 'feet']},
                      'miles': {'convert_options': ['km']},
                      'km': {'convert_options': ['mile']}
                      }

    @staticmethod
    def fix_output(result):
        return "%.3f" % result

    def miles_to_km(self, unit):
        return self.fix_output(unit * 1.609344)

    def km_to_miles(self, unit):
        return self.fix_output(unit / 1.609344)

    def cm_to_feet(self, unit):
        return self.fix_output(unit / 30.48)

    def cm_to_inches(self, unit):
        return self.fix_output(unit / 2.54)

    def cm_to_mm(self, unit):
        return self.fix_output(unit * 10)

    def cm_to_meter(self, unit):
        return self.fix_output(unit / 100)

    def mm_to_cm(self, unit):
        return self.fix_output(unit / 10)

    def mm_to_feet(self, unit):
        return self.fix_output(unit / 304.8)

    def mm_to_inches(self, unit):
        return self.fix_output(unit / 25.4)

    def meter_to_feet(self, unit):
        return self.fix_output(unit / 0.3048)

    def meter_to_inches(self, unit):
        return self.fix_output(unit / 0.0254)

    def feet_to_cm(self, unit):
        return self.fix_output(unit * 30.48)

    def feet_to_mm(self, unit):
        return self.fix_output(unit * 304.8)

    def feet_to_inches(self, unit):
        return self.fix_output(unit * 12)

    def feet_to_meter(self, unit):
        return self.fix_output(unit * 0.3048)

    def inches_to_cm(self, unit):
        return self.fix_output(unit * 2.54)

    def inches_to_feet(self, unit):
        return self.fix_output(unit / 12)

    def inches_to_meters(self, unit):
        return self.fix_output(unit * 0.0254)

    def inches_to_mm(self, unit):
        return self.fix_output(unit * 25.4)
