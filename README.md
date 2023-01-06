# Bitcoin-Wallet
A bitcoin wallet project written in Python using the Bitcoinlib library.




Testing
========

To test this wallet i did the following:

1) Generate new bitcoin wallet:

```
generate_new_wallet("a")
```

Output: 

```
Generating new wallet called "a"...
<Network: bitcoin>

This is your new wallet's seed phrase:
--------------------------------------

The seed will be displayed here.

-------------------------------------
Write these words down on a peice of
paper and keep them safe and secure!
```

2) Derive public key from wallet to recieve coins:

```
recieve_coins("a")
```

Output:

```
-------------------------------------
Receiving wallet name: "a"
Deposit coins to this address: "15hk6ZBRqKNsKXz3igZ7o8qnYkHoQgqgWK"
-------------------------------------
```

3) Send coins to this address:

- For this step i used an external wallet and sent 0.001 BTC (£14 / $16) to the wallet.

4) Check wallet balance:

```
print_wallet_balance("a")
```

Output:

```
-------------------------------------
Wallet name:     "a"
Wallet balance:  80000.0 (8000000000000 Sats)
-------------------------------------
```

4) Make new wallet to send coins too.

5) Send coins to newly created wallet:

```
-------------------------------------
Receiving wallet name: "b"
Deposit coins to this address: "1GpTboUKAWgs2yGaNhZYTsDGNbqwxYGJUp"
-------------------------------------
```

```
send_coins("a", "1GpTboUKAWgs2yGaNhZYTsDGNbqwxYGJUp",10000)

```

6) Check wallet balance:

```
print_wallet_balance("b")
```

Output:

```
-------------------------------------
Wallet name:     "b"
Wallet balance:  10000.0 (1000000000000 Sats)
-------------------------------------
```



