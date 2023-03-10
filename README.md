# Bitcoin-Wallet
A bitcoin wallet project written in Python using the Bitcoinlib library.


Features
=========

- Generate Hierarchical Deterministic (HD) Wallets
- Options To Create Bitcoin Testnet or Bitcoin Mainnet wallets 
- Customisable Wallet Seed Entropy 
- Wipe Local Wallet Data
- Import Wallet Using Seed Phrase
- Show Wallet Balance
- Send And Receive Coins

Installation
=============

- Run ```git clone https://github.com/programmer838/Bitcoin-Wallet/```
- Run ```cd Bitcoin-Wallet```
- Then run ```pip install -r requirements.txt```
- Finally to run the program type ```python3 wallet.py```

Usage
========


- Once the program is started a set of options is shown to the user:

```
---------------------------------------
Welcome to Bitcoin-Wallet by Qasim Ijaz
---------------------------------------

1 - Import wallet
2 - Create a new wallet
3 - Show all wallets
4 - Show wallet balance
5 - Receive funds
6 - Send funds
7 - Delete all local wallets
8 - Exit

Enter an option: 
```

- Users can enter options (1-8) and the program will allow the user to do what the corresponding text says.


To showcase the features i will send coins from one wallet to another:

1) Create 2 BTC testnet wallets:

```
generate_new_wallet()
generate_new_wallet()
```

Output:

```
Enter a wallet name:  wallet_A
Enter wallet network ("bitcoin" or "testnet"): testnet
Enter seed phrase strength (128 or 256): 128

Generating new wallet called "wallet_A"...

<Network: testnet>

This is your new wallet's seed phrase:
--------------------------------------

Your seed phrase will be displayed here.

-------------------------------------
Write these words down on a peice of
paper and keep them safe and secure!

Enter a wallet name:  wallet_B
Enter wallet network ("bitcoin" or "testnet"): testnet
Enter seed phrase strength (128 or 256): 128

Generating new wallet called "wallet_B"...

<Network: testnet>

This is your new wallet's seed phrase:
--------------------------------------

Your seed phrase will be displayed here.

-------------------------------------
Write these words down on a peice of
paper and keep them safe and secure!
```

2) Derive addresses to receive coins

```
receive_coins()
receive_coins()
```

Output:

```
Enter wallet name: wallet_A
-------------------------------------
Receiving wallet name: "wallet_A".
Deposit coins to this address: "mxCmSiMAbDAEoUxeU1EoToLTJmt9t2LcmW".
-------------------------------------
Enter wallet name: wallet_B
-------------------------------------
Receiving wallet name: "wallet_B".
Deposit coins to this address: "mhPTUtcGhSQB9dKAez7zVzoGmga9q2wspa".
-------------------------------------
```

3) Fund ```wallet_A```

- Visit a Bitcoin testnet faucet like https://coinfaucet.eu/en/btc-testnet/
- Paste address into faucet

![Screenshot from 2023-01-07 00-08-07](https://user-images.githubusercontent.com/71629437/211120361-ab9123c5-4b93-4488-a0ae-7ab669003abc.png)


4) Check the transaction was successful by printing wallet balance

```
print_wallet_balance()
```

Output:
```
Enter wallet name: wallet_A
Retrieving updated wallet balance...
Nearly done...

-------------------------------------
Wallet name:     "wallet_A"
Wallet balance:  0.01666225 BTC (1666225 sat)
-------------------------------------
```

5) Send coins to ```wallet_B``` using ```wallet_A``` funds

```
send_coins()
```

Output:
```
Enter wallet name to send funds from: wallet_A
Enter address to send funds to: mhPTUtcGhSQB9dKAez7zVzoGmga9q2wspa
Enter amount to send: 1666
Transaction success!
```


6) Check if coins arrived at ```wallet_B```

```
print_wallet_balance()
```

Output:

```
Enter wallet name: wallet_B
Retrieving updated wallet balance...
Nearly done...

-------------------------------------
Wallet name:     "wallet_B"
Wallet balance:  0.00001666 BTC (1666 sat)
-------------------------------------
```

Contributors
======
Qasim Ijaz --- Author
