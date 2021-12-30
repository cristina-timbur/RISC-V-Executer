# RISC-V Executer 

## 🥇 About the Project

Implemented a python script <a href="riscv-executer.py">**riscv-executer.py**</a>   which executes files with risc-v machine code. The goal of our project is to highlight the following steps:  
- IF : instruction fetch  
- ID : instruction decode  
- EX : execute  
- MEM : memory  
- WB  : write back  
    

## Usage

Choose a file from <a href="teste">**teste**</a> and run the python script as shown below    
  *&nbsp;&nbsp;&nbsp;&nbsp; // instead of 'file_name', write your own chosen file name*
```bash
python riscv-executer.py file_name
```

## Solution

Loaded the source code into a byte array. A memory address was associated to every byte, imitating
the real memory. Fetched 4 bytes which form the current instruction from memory location indicated by program_counter (IF part).
Executed the instruction based on the all the possible formats:   

- R-Type : slli, srl, xor, rem  
- S-Type : sw  
- I-Type : lw, addi, ori, ecall  
- B-Type : beq, bne  
- U-Type : lui, auipc  
- J-Type : jal  


### _Note_
 
- _li, mv, nop are implemented as addi_
- _beqz is implemented as beq_
- _j is implemented as jal_
 

After every test a message is printed although the source code does not demand it.
As a remark, there are some exceptions in the tests such as division by zero, register zero interpreted as a destination register.
When encountered, an error message is displayed on the screen and program_counter jumps to the fail label.  






## Copyright © 2021

@vl4dio4n &nbsp;@cristina-timbur 

***
*<p align="center"><a>FMI UniBuc 2021</a></p>* 

<p align="right">(<a href="#top">Back to Top</a>)</p>
