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

Usage
========

To showcase the features i will send coins from one wallet to another:

- Create 2 BTC testnet wallets:

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



