README for yahooticker

Contents
1. Description
2. Compilation
3. Installation
4. Invocation
5. Version History


1. Description
yahooticker is a LibreOffice Calc Add-In function that queries yahoo.finance
for the current market value of the instrument passed to it.

2. Compilation
If you want to compile the .oxt yourself, you will need the LibreOffice SDK.

Generating the .oxt is a two step process:
1. Run the initiate_lo_sdk.sh script: ./initiate_lo_sdk.sh
2. Run the generate_oxt.sh script: ./generate_oxt.sh

The resulting yahooticker.oxt can then be found in the current folder.

3. Installation
In the LibreOffice Menu go to Tools->Extension Manager
Then click on Add... and go to the location of yahooticker.oxt. Click on open
to register the AddOn with LibreOffice.

4. Invocation
Generell invocation works as follows:

=YAHOOTICKER("instrument_to_query")

instrument_to_query in this case is the last part of the the url of the instrument, whose price you would like to obtain.

Assume for example that you are interested in tracking the stockprice of Alphabet Inc.
The path to this instrument on yahoo finance is: 
https://finance.yahoo.com/quote/GOOG?p=GOOG

To obtain the same price in a Calc spreadsheet invoke yahooticker and pass the
string behind the last slash to it.

=YAHOOTICKER("GOOG?p=GOOG")

Note that the call may fail, when the exchange is closed.

5. Version History
yahooticker V 0.1 was released on 11.25.2017
