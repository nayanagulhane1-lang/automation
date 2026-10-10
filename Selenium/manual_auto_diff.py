
# ## 1. Manual Testing vs Automation Testing

# | Manual Testing                                                 | Automation Testing                                                          |
# | -------------------------------------------------------------- | --------------------------------------------------------------------------- |
# | A tester checks the application manually.                      | A tester writes scripts to check the application automatically.             |
# | Takes more time for repetitive testing.                        | Saves time when the same tests run repeatedly.                              |
# | Best for exploratory testing and checking the user experience. | Best for regression testing and repetitive test scenarios.                  |
# | Human observation is important.                                | Scripts compare actual results with expected results.                       |
# | Example: Manually checking whether a button looks good.        | Example: Automatically checking whether a button works after every release. |

# ## 2. Three scenarios where automation saves time

# [Improving Zomato's Cart Experience with Simplified UI | Aditya Saini posted on the topic | LinkedIn](https://images.openai.com/static-rsc-4/lVnelUyOvpUTIDUo4uC9JwRIUq22d4QlWYZcwbUo9cUuvQlPActILGQ5k_w6IuE8WwHOtKXtRKn3yuaMU799XuRzk3E5LfsSNdShZ8wm3WFLSnpYORvUghDuy9V0nXESm9cCUCe9O4nESSf95JCkk2XruJNBiji8MjNIlYgvR2A?purpose=inline)

# Scenario 1: Zomato — Food ordering and checkout

# Test: Login, search for a restaurant, add food to the cart, verify the total price, and proceed to checkout.

# - Manual: The tester repeats every step for each regression cycle.
# - Automation: A Selenium script repeats the flow and validates the cart total.

# Benefit: Saves time when testing the same flow after every code change.

# [Instagram App designs, themes, templates and downloadable graphic elements on Dribbble](https://images.openai.com/static-rsc-4/4UhuoSyE9C7V-DT4HlEnmFXavR8M6JZAvEnP7CssVPz8kZndidIUO4ietj68fpUKkdoOnHi0TD5GzX4NQq9yypiAkO9EIB_dsOh5Z9vDlvcsBnLsmgpWrBiCPiVmshVEqoEvq7sl97OezLPS6XamLF-dkvHdN1Gjd8PyGVH5Dps?purpose=inline)

# Scenario 2: Instagram — Login functionality

# Test: Verify login with valid credentials, invalid passwords, empty fields, and locked or restricted accounts where applicable.

# - Manual: The tester enters different combinations one by one.
# - Automation: A script runs multiple test cases and checks the expected error messages or successful login.

# Benefit: Quickly tests many input combinations after application updates.

# [Download IRCTC Rail Connect 4.2.58 for Android - Filehippo.com](https://images.openai.com/static-rsc-4/8p7hhW8j0XIEfxDvcQmH52CnjX29Cws8IP_zktuGFUXH06Kl57DF7_uXuq48sxvEAOEGLI-I5WvGh5uaLvufHO8osKUga18qvFVXQpsnW73_s9FrjQZuBIh8oKw1ex9eduiKVTMKkGMu7CYufBmtA9xtGYjo6eA0zkfmQARk8d4?purpose=inline)

# Scenario 3: IRCTC — Train search and availability

# Test: Search trains using different source stations, destinations, travel dates, and passenger combinations.

# - Manual: The tester repeats the searches individually.
# - Automation: A script checks multiple test combinations and validates the displayed results against expected test data.

# Benefit: Reduces repetitive work and helps detect regression defects quickly.
