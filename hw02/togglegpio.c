#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "gpio-utils.h"

int main()
{
  int state = True;
	int onOffTime=100;	// Time in micro sec to keep the signal on/off
	int led = 60;
  int led_fd;

	gpio_export(led);
	gpio_set_dir(led, "out");
  led_fd = gpio_fd_open(led, O_WRONLY);
	
	while(1)
	{
		state = !state;
		lseek(led_fd, 0, SEEK_SET);
		if (state)
			write(led_fd, "1", 2);
		else
			write(led_fd, "0", 2);

		usleep(onOffTime);
	}
	led_fd_close(led_fd);
	
	return 0;
}
