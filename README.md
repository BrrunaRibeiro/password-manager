## Libraries 

* Gspred
* Google-Auth(Credentials class only)

## Fixed bugs
* The gspread' update() method was the first option. However it genereated the error:
``` UserWarning: [Deprecated][in version 6.0.0]: method signature will change to: 'Worksheet.update(value = [[]], range_name=)' arguments 'range_name' and 'values' will swap, values will be mandatory of type: 'list(list(...))'
  warnings.warn( ```
 I seached for a solution both online and with Code Institute Tutors, they advised to look for an alternative code as there is an issue with the method signature from certain versions of the gspread library.
 As an alternative 