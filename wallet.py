import sys
from bitcoinlib.keys import Key
from bitcoinlib.keys import HDKey
from bitcoinlib.mnemonic import Mnemonic
from bitcoinlib.wallets import *
from bitcoinlib.values import *


def delete_all_wallets():

    wallets = wallets_list()
    wallet_names = (item['name'] for item in wallets)

    choice = input("Are you sure you want to remove all wallet data? (Y/N): ")

    if (choice == 'Y'):
        for i in wallet_names:
            wallet_delete(i, force="True")
        print("All wallets deleted successfully")

def print_wallets():
   
    wallets = wallets_list()
    wallet_names = (item['name'] for item in wallets)

    print("\nWallets: \n")    

    for i in wallet_names:
        print(f"- \"{i}\"")

def generate_new_wallet():
     
    wallet_name, netwrk, strngth = None, None, 0

    wallet_name = input("Enter a wallet name:  ")
    
    while (netwrk not in ['bitcoin', 'testnet']):
           netwrk = input("Enter wallet network (\"bitcoin\" or \"testnet\"): ")

    while (strngth not in [128, 256]):
           try:    
              strngth = int(input("Enter seed phrase strength (128 or 256): "))
           except:
              pass

    if (not wallet_exists(wallet_name)):
     
        try: 
           passphrase = Mnemonic().generate(strngth)
           wif = HDKey.from_passphrase(passphrase)
           wallet = wallet_create_or_open(wallet_name, wif.private_hex, network=netwrk)
        except Exception as e:
           print(f"Error: Failed to create wallet called \"{wallet_name}\"")
           print(e)
           return

        print(f"\nGenerating new wallet called \"{wallet_name}\"...\n")   
        print(f"{wallet.network}\n")

        print("This is your new wallet's seed phrase:")
        print("--------------------------------------\n") 
   
        for count, val in enumerate(passphrase.split(" ")):
            print(f"{count+1}) \"{val}\"", end = " ")
            if ((count+1) % 3 == 0):
                print('\n')

        print("-------------------------------------")    
        print("Write these words down on a peice of");
        print("paper and keep them safe and secure!\n")
    else:
        print(f"Error: Wallet with name \"{wallet_name}\" already exists.")

def import_wallet():

    wallet_name = input("Enter a wallet name: ")
    seed = input("Enter your seed phrase: ")

    if (not wallet_exists(wallet_name)):
        try:
           wif = HDKey.from_passphrase(seed)
           Wallet.create(wallet_name, wif.private_hex)
           print("\nWallet imported successfully!")
        except:
           print("Error: Seed phrase is invalid.")
           return
    else:
        print(f"Error: Wallet \"{wallet_name}\" already exists.")
    
def print_wallet_balance():
    
    wallet_name = input("Enter wallet name: ")    

    if (wallet_exists(wallet_name)):
        try: 
           print("Retrieving updated wallet balance...")
           wallet = wallet_create_or_open(wallet_name)
           wallet.balance_update_from_serviceprovider()
           print("Nearly done...\n")
           wallet.utxos_update()
        except Exception as e:
           print("Error: Failed to retrieve wallet balance.")
           return          

        val = Value.from_satoshi(wallet.balance(), network='bitcoin')         

        print("-------------------------------------")
        print(f"Wallet name:     \"{wallet_name}\"")
        print(f"Wallet balance:  {Value(val).str(1)} ({val})")
        print("-------------------------------------")
    else:
        print(f"Error: Wallet \"{wallet_name}\" does not exist.")  
     
def receive_coins():
 
    wallet_name = input("Enter wallet name: ")

    if (wallet_exists(wallet_name)):
        wallet = wallet_create_or_open(wallet_name)
        wallet.scan()
        new_key = wallet.new_key()
        print("-------------------------------------")
        print(f"Receiving wallet name: \"{wallet_name}\".")
        print(f"Deposit coins to this address: \"{new_key.address}\".")
        print("-------------------------------------")
   
    else:
        print(f"Error: Wallet \"{wallet_name}\" does not exist.")

def send_coins():
  
     wallet_name = input("Enter wallet name to send funds from: ")
     receiving_address = input("Enter address to send funds to: ")
     amount = 0     

     while (amount != 0):
            try:
               amount = 0
               amount = int(input("Enter amount to send: "))
            except:
               pass
 
     if (wallet_exists(wallet_name)):
         wallet = wallet_create_or_open(wallet_name)
         netwrk = 'bitcoin' if 'bitcoin' in str(wallet.network) else 'testnet'
         wallet.scan()

         wallet_val = value_to_satoshi(Value(wallet.balance())) 
         amount_val = value_to_satoshi(Value(amount))

         if (amount_val > wallet_val):
             print("Error: not enough funds in wallet \"{wallet_name}\"")

         try:
            transaction = wallet.send_to(receiving_address, amount, fee="normal", offline=False, network=netwrk)
         except Exception as e:
            print(f"Error: {e}")
            return

         if transaction:
            print("\nTransaction success!")
            print(f"Transaction ID: {transaction.txid}\n")
            transaction.info()
     else:
         print(f"Error: Wallet \"{wallet_name}\" does not exist.")

def exit_program():
    print("Exiting...")
    sys.exit()

def print_options():
    print("\n1 - Import wallet")
    print("2 - Create a new wallet")
    print("3 - Show all wallets")
    print("4 - Show wallet balance")
    print("5 - Receive funds")
    print("6 - Send funds")
    print("7 - Delete all local wallets")
    print("8 - Exit\n")
    

def main():

    print("---------------------------------------")   
    print("Welcome to Bitcoin-Wallet by Qasim Ijaz")
    print("---------------------------------------")

    option = 0
    functions = [import_wallet, generate_new_wallet, print_wallets, print_wallet_balance, 
                 receive_coins, send_coins, delete_all_wallets, exit_program]

    while (True):
          
           print_options()
           
           try:
              option = 0 
              option = int(input("Enter an option: "))
           except:
              print("Error: Invalid option.")
               
           if (option in [1,2,3,4,5,6,7,8]):
               functions[option-1]()

if __name__ == "__main__":
    main()

