#!/bin/bash

# TODO: Automate error checking and validate results

rm -f ABI_test.cc ABI_al.cc

clang -E all.h | python ../post_process_header.py | python ../make_abi_library.py > ABI_all.cc
clang -E abi_test.h | python ../post_process_header.py | python ../make_abi_library.py > ABI_test.cc
