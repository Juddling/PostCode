## Usage instructions

Please use Python 3

## Postcode Regular Expression

The given regular expression successfully validates all of the standard formats of UK postcode beginning with: AA9A, A9A, A9, A99, AA9 and AA99 (where A is a letter and 9 is a digit).
The ending format is always 9AA.

The regular expression is however too permissive, and will validate many postcodes which do not exist. 
For example, there are only 20 south-west districts in London, SW1 to SW20, however the regular expression will validate SW50 9AA.

### Special Case Postcodes

GIR 0AA is a special case postcode of Girobank. It has been hard coded into the regular expression so this postcode does validate.

Some non-geographic post codes will fail the validation, including the post code for Santa, XM4 5HQ.

SIQQ 1ZZ is an example of a UKode which fails validation. This is the post code for the South Georgia and the South Sandwich Islands overseas postc