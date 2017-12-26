#!/bin/sh

# Compile the .rdb file.
idlc -I /usr/lib64/libreoffice/sdk/idl idl/XYahooTicker.idl
regmerge idl/XYahooTicker.rdb /UCR idl/XYahooTicker.urd

# Delete the .urd file, as it's just of temporary need.
rm -v idl/XYahooTicker.urd

# Move the .rdb file to its destination.
mv -i idl/XYahooTicker.rdb ./

# In case there is an old .oxt file delete it.
rm -vf yahooticker.oxt

# zip the source files.
zip yahooticker.zip \
	META-INF/manifest.xml \
	ytCalcAddIn.xcu \
	XYahooTicker.rdb \
	description.xml \
	yahooticker.py

# An .oxt file is actually just a .zip file.
mv -i yahooticker.zip yahooticker.oxt

exit 0
