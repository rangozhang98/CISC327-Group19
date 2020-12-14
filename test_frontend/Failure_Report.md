### How we modified the template for testing

Originally, test_approach_2 ran the program with 3 arguments,
```
sys.argv = [
        'app.py',
        valid_account_list_file,
        transaction_summary_file]
```
which didn't follow the program input specifications.

We added a temp file for tickets, and a string for location (which doesn't matter for our tests).
```
sys.argv = [
        'main.py',
        'testCity',
        valid_account_list_file,
        valid_ticket_list_file
    ]
```

We also added a transaction array into our helper arguments, which 
are compared with the file created in the program.

## Failure Report
| Test Name | Purpose | Output error | Source code error | Changes made |
|-----------|---------|--------------|-------------------|--------------|
| R2_8_5 | Username can have spaces if they're not at the start/end | 'A Aa' not accepted | username rejected if it's not alphanumeric | code checks chars in username and accepts inside spaces|
| test_r4_2 | testing if a proper sell session begins                         | Output was supposed to exit back to landing after starting the sell   | Code did not properly filter invalid ticket names                                   | Added logical if statement to prevent certain invalid names from passing         |
| test_r4_3 | testing if a sell would complete with completely legal inputs   | Output did not allow for valid ticket name to pass the check          | Code did not allow for proper alphanumeric ticket names                             | Changed pre-existing statements to allow valid ticket names                      |
| test_r4_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for spaces at the end                                           | Changed code to prevent spaces at the end                                        |
| test_r4_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for symbols                                                     | Changed code to prevent symbols                                                  |
| test_r4_4 | testing different types of valid ticket names (tick et3)        | Output was not allowing valid ticket name (tick et3) to pass          | Code did not allow for spaces to be in the middle of the ticket name                | Changed code to allow only spaces to be allowed in the middle of the ticket name |
| test_r4_8 | testing different ways of writing dates                         | Output allowed for invalid date styles to pass                        | Code did not check for alphabetical dates                                           | Changed code to prevent letters from being a valid date                          |
| test_r4_8 | testing different non-existent dates                            | Output allowed for non-existent dates (Feb 31)                        | Code did not care what month it was and only checked for days greater than the 31st | Changed code to accurately reflect the number of days in each month              |
| test_r4_8 | testing leap years (Feb 29, 2020)                               | Output did not allow for Feb 29                                       | Code did not allow Feb to have more than 28 days                                    | Changed code to add a case to allow leap years to have 29 days in Feb            |
| test_r5_2 | testing if a proper sbuy session begins                         | Output was supposed to exit back to landing after starting the buy    | Code did not properly filter invalid ticket names                                   | Added logical if statement to prevent certain invalid names from passing         |
| test_r5_3 | testing if a buy would complete with completely legal inputs    | Output did not allow for valid ticket name to pass the check          | Code did not allow for proper alphanumeric ticket names                             | Changed pre-existing statements to allow valid ticket names                      |
| test_r5_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for spaces at the end                                           | Changed code to prevent spaces at the end                                        |
| test_r5_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for symbols                                                     | Changed code to prevent symbols                                                  |
| test_r5_4 | testing different types of valid ticket names (tick et3)        | Output was not allowing valid ticket name (tick et3) to pass          | Code did not allow for spaces to be in the middle of the ticket name                | Changed code to allow only spaces to be allowed in the middle of the ticket name |
| test_r6_2 | testing if a proper update session begins                       | Output was supposed to exit back to landing after starting the update | Code did not properly filter invalid ticket names                                   | Added logical if statement to prevent certain invalid names from passing         |
| test_r6_3 | testing if a update would complete with completely legal inputs | Output did not allow for valid ticket name to pass the check          | Code did not allow for proper alphanumeric ticket names                             | Changed pre-existing statements to allow valid ticket names                      |
| test_r6_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for spaces at the end                                           | Changed code to prevent spaces at the end                                        |
| test_r6_4 | testing different types of invalid ticket names                 | Output was allowing invalid ticket names to pass                      | Code did not filter for symbols                                                     | Changed code to prevent symbols                                                  |
| test_r6_4 | testing different types of valid ticket names (tick et3)        | Output was not allowing valid ticket name (tick et3) to pass          | Code did not allow for spaces to be in the middle of the ticket name                | Changed code to allow only spaces to be allowed in the middle of the ticket name |
| test_r6_8 | testing different ways of writing dates                         | Output allowed for invalid date styles to pass                        | Code did not check for alphabetical dates                                           | Changed code to prevent letters from being a valid date                          |
| test_r6_8 | testing different non-existent dates                            | Output allowed for non-existent dates (Feb 31)                        | Code did not care what month it was and only checked for days greater than the 31st | Changed code to accurately reflect the number of days in each month              |
| test_r6_8 | testing leap years (Feb 29, 2020)                               | Output did not allow for Feb 29                                       | Code did not allow Feb to have more than 28 days                                    | Changed code to add a case to allow leap years to have 29 days in Feb            |