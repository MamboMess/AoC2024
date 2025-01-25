# How to Run the Retrofitted solution
1. configure the `venv` and `requirements.txt` by running: `./d0 -b`
2. Run d0 by calling `./d0 -d<DAY> -p<PART> -i<PATH_TO_INPUT>

## NOTE
* This script runs nearly identical to my `d0`
* Day 14 has an output file that is dumped to tmp. It is not needed for anything.
* Days that have only a part 1 will throw a `NotImplementedError` if called with `-p2`
* The `venv` was needed to get matplotlib working on my ancient MAC and may
effect timing. **IF YOU ARE FELING AMBITIOUS**, you could delete lines 15 & 
21 of `d0`. But matplotlib and numpy might be upset with your choice.

**Good Luck!**
