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
| Ur test | Ur purpose | ur output err | ur code err| ur changes |