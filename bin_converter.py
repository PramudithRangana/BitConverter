""" Convert Data """


class ConvertData:

    @staticmethod
    def string_bits(strWord=''):
        return [bin(ord(x))[2:].zfill(8) for x in strWord]  # Convert to - Ascii -

    # __________________________________________________________________________
    @staticmethod
    def bit_strings(b):
        return ''.join([chr(int(x, 2)) for x in b])  # Convert to - character -

    @staticmethod
    def bit_oct(b):
        return ' '.join([oct(int(x, 2)).replace('0o', '') for x in b])  # Convert to - octa decimal -

    @staticmethod
    def bit_int(b):
        return ' '.join([str(int(x, 2)) for x in b])  # Convert to - decimal string -

    @staticmethod
    def bit_hex(b):
        return ' '.join([hex(int(x, 2)).replace('0x', '') for x in b])  # Convert to - hex decimal -

    @staticmethod
    def str_bin(b):
        return bin(int(b)).replace('0b', '').zfill(8)  # Convert to - binary -

    @staticmethod
    def str_oct(b):
        return oct(int(b)).replace('0o', '')  # Convert to - octa decimal -

    @staticmethod
    def str_hex(b):
        return hex(int(b)).replace('0x', '')  # Convert to - hex decimal -


''' Show Data '''


class ViewData:
    c_d = ConvertData()

    def view_data_for_str(self, GetString):

        b = self.c_d.string_bits(GetString)
        print('Binary Representation      :', b, '\n')

        converted_str = self.c_d.bit_strings(b)
        print('ASCII Character            :', converted_str, '\n')

        converted_oct = self.c_d.bit_oct(b)
        print('Oct-decimal Representation :', converted_oct, '\n')

        converted_int = self.c_d.bit_int(b)
        print('Decimal Representation     :', converted_int, '\n')

        converted_hex = self.c_d.bit_hex(b)
        print('Hexadecimal Representation :', converted_hex, '\n')

        self.input_string()

    def view_data_for_int(self, i):

        int_to_bin = self.c_d.str_bin(i)
        print('BINARY CODE :', int_to_bin, '\n')

        int_to_oct = self.c_d.str_oct(i)
        print('int to oct  :', int_to_oct, '\n')

        int_to_hex = self.c_d.str_hex(i)
        print('int to hex  :', int_to_hex, '\n')

        self.input_string()

    def input_string(self):
        st = input('>> : ')
        if st == 'exit':
            exit()
        else:
            try:
                st = int(st)
                self.view_data_for_int(st)
            except:
                self.view_data_for_str(st)


if __name__ == '__main__':
    obj = ViewData()
    obj.input_string()

s = '''Hello this is ASCII CODE from \nhello world'''
