obj-m+=led.o

# -----------------------
# ------ make all -------
# -----------------------
all:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) modules

# ----------------------
# ----- clean all ------
# ----------------------
clean:
	make -C /lib/modules/$(shell uname -r)/build/ M=$(PWD) clean
