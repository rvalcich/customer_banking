# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('How much would you like to deposit for your savings account? '))
    savings_interest = float(input('How much of an (annual) interest rate would you like your savings account to have? '))
    savings_maturity = int(input('How long (in months) would you like to have the account for? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Your savings acocunt now has a balance of ${updated_savings_balance: ,.2f} '
          +f'with a total of ${interest_earned: ,.2f} earned interest '
          +f'over the {savings_maturity} month period')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('How much would you like to deposit for your CD? '))
    cd_interest = float(input('How much of an (annual) interest rate would you like your CD to have? '))
    cd_maturity = int(input('How long (in months) would you like to have the CD for? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'Your CD now has ${updated_cd_balance: ,.2f} '
          +f'with a total of ${interest_earned: ,.2f} '
          +f'earned interest over the {cd_maturity} month period')

if __name__ == "__main__":
    # Call the main function.
    main()
