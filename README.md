# Custom Hash Algorithm vs SHA-256
Name: Vijay S P  
USN: 24MSRDF037  

# Ojective
A custom hash function that returns a fixed 32-character hash, and compare it with SHA-256.

# Algorithm Logic

- Uses ASCII conversion
- Multiplies by index + 1
- Applies modulo for mixing
- Compresses into 32-character hex output

# Sample Output Table

| Input | Custom Hash                      | SHA-256 (first 32 chars)         |
| hello | 0708212c460000000000000000000000 | 2cf24dba5fb0a30e26e83b2ac5b9e29e |
| Hello | 4808212c460000000000000000000000 | 185f8db32271fe25f561a6fc938b2e26 |

# Screenshots
Source Code:![alt text](<Screenshot (154)-1.png>)
Output     :![alt text](image.png)

# Comparison

- Same input → Same hash ✔️  
- Small change → Very different hash ✔️  
- SHA-256 is cryptographically stronger  
- Custom hash is simpler, educational
