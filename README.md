# ST-Manager
Screen-Time managing tool

## Install
copy to your terminal: `git clone https://github.com/Idanos99/ST-Manager`

## How to use

`python ST-M/ST-M/main.py`

following flags can be used

`-h, --help`            show this help message and exit

`-m MIN, --min MIN`     set number of minutes to work. default: 20.

`-s SEC, --sec SEC`     set number of seconds to rest. default: 20.

`-l LOOP, --loop LOOP`  how many times repeat the timer. (-1 for nonstop)
                        default: -1.
                        
`-S, --suspend`         suspend the screen after the work time is over.
                        (disable rest and loop)
                        
`-q, --quiet`           disable alarm in the last minutes
