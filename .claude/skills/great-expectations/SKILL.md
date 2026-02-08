---
name: great-expectations
description: Data validation patterns with Great Expectations
---

# Great Expectations Skill

## When to Use
- Validating data schema before training
- Checking data distributions
- Creating expectation suites for pipelines

## Pattern

```python
import great_expectations as gx

context = gx.get_context()

# Create a data source
datasource = context.data_sources.add_pandas("transactions")

# Define expectations
suite = context.add_expectation_suite("fraud_suite")
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeOfType(column="amount", type_="float")
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToBeBetween(column="amount", min_value=0, max_value=1000000)
)
suite.add_expectation(
    gx.expectations.ExpectColumnValuesToNotBeNull(column="merchant_id")
)
```

## Important
- ALWAYS check docs/research/ge-latest.md for current API
- Validate data BEFORE any training step
- Store expectation suites in `great_expectations/expectations/`
