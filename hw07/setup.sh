#define BLYNK_TEMPLATE_ID "TMPLBNJZ_xD6"
#define BLYNK_DEVICE_NAME "Beagle Bone Connection"
#define BLYNK_AUTH_TOKEN "P7cwZgK-waBwdYRPwry9P-UXZ_OoMYDR"

export BLYNK_AUTH_TOKEN='P7cwZgK-waBwdYRPwry9P-UXZ_OoMYDR'

I2C=/sys/class/i2c-adapter/i2c-2
echo temp101 0x48 > $I2C/new_device
