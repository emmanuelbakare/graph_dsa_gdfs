class PrintColor:
    
    def red(text):
        print(f"\033[91m{text}\033[0m")
    
    def green(text):
        print(f"\033[92m{text}\033[0m")
        
    def yellow(text):
        print(f"\033[93m{text}\033[0m")
        
    def blue(text):
        print(f"\033[94m{text}\033[0m")
        
    def purple(text):
        print(f"\033[95m{text}\033[0m")
        
    def cyan(text):
        print(f"\033[96m{text}\033[0m")


def heading(title):
    print()
    print()
    # print(f'====== {title.upper()} ======')
    print(title.upper().center(50,'*'))
    
def get_input(msg='Enter Value: ', itype=str):
        
    value=input(msg)
    
    # Exit on no Entry: 
    if len(value.strip())==0: 
        print('No value entered. exiting...')
        exit()
    # if the value entered is not a string, then try to convert it before returning it
    #iType attribute tell what type to convert it to
    if itype is not str:
        try:
            value=itype(value)
        except Exception as e:
            print(f'expecting type {itype}\n{e}')
            return False
    # print(f"Value {converted_value} is {itype}")
    return value
        