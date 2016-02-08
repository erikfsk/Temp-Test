from main_temp import LivePlot
import argparse
import serial


#
arg_save = None
arg_clear = False
arg_clear_file = None

parser = argparse.ArgumentParser(
    description="""UI for Temperature logging. Running this script without any args, will give a live plot and values in the terminal"""
)


#save data
parser.add_argument("-d", "--default", help="default setup: Clear data from data.txt and save data to data.txt ",
                    action="store_true")
#save data
parser.add_argument("-s", "--save", help="Save data to the data.txt file",
                    action="store_true")
#clear previously saved data
parser.add_argument("-c", "--clear", help="default clearfile",
                    action="store_true")
#define save file
parser.add_argument("-o", "--outfile", help="define txt file for data output. This will automaticly save data too",
                    action="store_true")
#might be implemented later
parser.add_argument("-t", "--txt", help="only saving data to txt (NO PLOT). THIS FEATURE IS NOT IMPLEMENTED! ",
                    action="store_true")

args = parser.parse_args()


if args.save:
	arg_save = "data.txt"

if args.default:
	arg_clear = True
	arg_save = "data.txt"

if args.clear:
	arg_clear = True
	arg_clear_file = raw_input("clear_file = ")

if args.outfile:
	arg_save = raw_input("pleas write the name of the file you would like your output to be writen in: ")

if __name__ == '__main__':    
	device = serial.Serial(port='/dev/tty.usbmodem1411', baudrate=9600) # R_Pi = /dev/ttyACM0 
	p = LivePlot(device, float, verb=False,save=arg_save, clear=arg_clear, clear_file=arg_clear_file)
	p.start()
	raw_input()
	p.join()
