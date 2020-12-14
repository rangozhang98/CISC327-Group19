### How we modified the template for testing

Originally, test_approach_2 ran the program with 3 arguments,
```
sys.argv = [
        'app.py',
        valid_account_list_file,
        transaction_summary_file]
```
which didn't follow the program input specifications.

We changed the arguments to test multiple transaction files, represented with a_transactions.csv and b_transactions.csv
```
sys.argv = [
        'backend.py',
        temp_a_transactions,
        temp_b_transactions
    ]
```

We also changed the arguments in the function to reflect the new inputs, 
which didn't require terminal input.

## Failure Report
| Test Name | Purpose      | Output Error                                          | Source Code Error                                         | Changes Made                                                      |
|-----------|--------------|-------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|
| test_buy       | Test buy function | Did not successfully fulfill the backend requirements | Buy function did not compare the proper values            | changed the index so that the value is being compared             |
| test_sell       | Test sell function | Did not successfully fulfill the backend requirements | Sell function did not compare the proper values           | changed the index so that the value is being compared             |
| test_buy       | Test buy function | Did not successfully fulfill the backend requirements | Buy function did not perform the proper value adjustments | changed the arithmetic to accurately calculate the new balance    |
| test_sell      | Test sell function | Did not successfully fulfill the backend requirements | Sell function did not operate as it should have           | rewrote function to perform according to the guidelines specified |
|  test_registration   | Test registration | Did not successfully fulfill the backend requirements | Wrong accounts file accessed   | Enclosed file access in a try/except to adjust for outside pytest access |                                                       |                                                           |                                                                   |
```
