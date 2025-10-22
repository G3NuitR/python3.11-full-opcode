# 108 / 110 opcode will be generated for compile this file.
# checked by using python.godbolt.org

# Instruction opcodes for compiled code
# Blank lines correspond to available opcodes

def_op('CACHE', 0)  # FIXME

# def_op('POP_TOP', 1)
# def_op('PUSH_NULL', 2)
a()

# def_op('NOP', 9)
while True:
    break

# def_op('UNARY_POSITIVE', 10)
+ a

# def_op('UNARY_NEGATIVE', 11)
- a

# def_op('UNARY_NOT', 12)
not a

# def_op('UNARY_INVERT', 15)
~a

# def_op('BINARY_SUBSCR', 25)
a[1]

# def_op('MATCH_MAPPING', 31)
# def_op('MATCH_SEQUENCE', 32)
# def_op('MATCH_KEYS', 33)
match {"k": 1}:  # MATCH_MAPPING / MATCH_KEYS
    case {"k": 1}:
        pass


# def_op('GET_LEN', 30)
match [1, 2]:  # MATCH_SEQUENCE
    case [1, 2]:
        pass


# def_op('PUSH_EXC_INFO', 35)
# def_op('CHECK_EXC_MATCH', 36)
# def_op('POP_EXCEPT', 89)
try:  # PUSH_EXC_INFO, CHECK_EXC_MATCH, POP_EXCEPT
    raise ValueError("boom")
except ValueError as exc:
    pass

# def_op('CHECK_EG_MATCH', 37)
# def_op('PREP_RERAISE_STAR', 88)
try:
    raise ExceptionGroup(
        'exception group',
        [
            TypeError('TypeError in ExceptionGroup'),
            ValueError('ValueError in ExceptionGroup')
        ]
    )
except* TypeError as e:
    if m.pi > 3:
        raise e

# def_op('WITH_EXCEPT_START', 49)
# def_op('BEFORE_WITH', 53)
with open("fuck you python 3.11") as f:
    print()

# def_op('GET_AITER', 50)
# def_op('GET_ANEXT', 51)
# def_op('BEFORE_ASYNC_WITH', 52)
# def_op('END_ASYNC_FOR', 54)
import contextlib
from typing import Iterable
async def async_samples(async_iterable: Iterable[int]) -> None:
    """Emit async-specific opcodes."""

    async for _ in async_iterable:  # GET_AITER, GET_ANEXT, END_ASYNC_FOR
        continue

    async with contextlib.AsyncExitStack():  # BEFORE_ASYNC_WITH
        pass


# def_op('STORE_SUBSCR', 60)
GLOBAL_MUTABLE_LIST[0] = 10  # STORE_SUBSCR

# def_op('DELETE_SUBSCR', 61)
del GLOBAL_MUTABLE_LIST[0]  # DELETE_SUBSCR

# def_op('GET_ITER', 68)
for item in seq:
    pass

# def_op('GET_YIELD_FROM_ITER', 69)
# def_op('RETURN_GENERATOR', 75)
# def_op('YIELD_VALUE', 86)
def simple_generator():
    yield from [2, 3]  # GET_YIELD_FROM_ITER

def_op('PRINT_EXPR', 70)  # FIXME

# def_op('LOAD_BUILD_CLASS', 71)
class _C:
    pass
_C()

# def_op('LOAD_ASSERTION_ERROR', 74)
assert m.pi > 3

# def_op('LIST_TO_TUPLE', 82)
(1, *a, *b)

# def_op('RETURN_VALUE', 83)
def f():
    return 1

# def_op('IMPORT_STAR', 84)
from typing import *

# def_op('SETUP_ANNOTATIONS', 85)
class C:
    field: 'annotation'

# def_op('ASYNC_GEN_WRAP', 87)
async def async_generator():
    yield 1  # ASYNC_GEN_WRAP

##########################
### HAVE_ARGUMENT = 90 ### # Opcodes from here have an argument:
##########################

# name_op('STORE_NAME', 90)       # Index in name list
a = 1

# name_op('DELETE_NAME', 91)      # ""
del a

# def_op('UNPACK_SEQUENCE', 92)   # Number of tuple items
a, b = 1, 2

# jrel_op('FOR_ITER', 93)
for i in a:
    pass

# def_op('UNPACK_EX', 94)
a, *b = A

# name_op('STORE_ATTR', 95)       # Index in name list
a.a = 1

# name_op('DELETE_ATTR', 96)      # ""
del a.a

# name_op('STORE_GLOBAL', 97)     # ""
def a():
    global aa
    aa = 1

# name_op('DELETE_GLOBAL', 98)    # ""
def a():
    global aa
    del aa

# def_op('SWAP', 99)
STACK[-i], STACK[-1] = STACK[-1], STACK[-i]

# def_op('LOAD_CONST', 100)       # Index in const list
# hasconst.append(100)
a = 123

# name_op('LOAD_NAME', 101)       # Index in name list
a

# def_op('BUILD_TUPLE', 102)      # Number of tuple items
(a, )

# def_op('BUILD_LIST', 103)       # Number of list items
[]

# def_op('BUILD_SET', 104)        # Number of set items
{1}

# def_op('BUILD_MAP', 105)        # Number of dict entries
{}

# name_op('LOAD_ATTR', 106)       # Index in name list
a.a

# def_op('COMPARE_OP', 107)       # Comparison operator
# hascompare.append(107)
a == a

# name_op('IMPORT_NAME', 108)     # Index in name list
# name_op('IMPORT_FROM', 109)     # Index in name list
from b import a

# jrel_op('JUMP_FORWARD', 110)    # Number of words to skip
try:
    raise Exception("boom")
except Exception as e:
    pass

# jrel_op('JUMP_IF_FALSE_OR_POP', 111) # Number of words to skip
a <= b and b < c

# jrel_op('JUMP_IF_TRUE_OR_POP', 112)  # ""
a <= b or b < c

# jrel_op('POP_JUMP_FORWARD_IF_FALSE', 114)
if a > b:
    pass

# jrel_op('POP_JUMP_FORWARD_IF_TRUE', 115)
if not b: 
    pass

# name_op('LOAD_GLOBAL', 116)     # Index in name list
def a():
    global b
    return b

# def_op('IS_OP', 117)
a is b

# def_op('CONTAINS_OP', 118)
1 in seq  # CONTAINS_OP

# def_op('RERAISE', 119)
try:
    raise Exception("boom")
except ImportError:
    pass

# def_op('COPY', 120)
try:
    raise ValueError("boom")
except ValueError as exc:
    pass


# def_op('BINARY_OP', 122)
a + b  # BINARY_OP

# jrel_op('SEND', 123) # Number of bytes to skip
async def async_samples(async_iterable: Iterable[int]) -> None:
    """Emit async-specific opcodes."""

    async for _ in async_iterable:  # GET_AITER, GET_ANEXT, END_ASYNC_FOR
        continue

# def_op('LOAD_FAST', 124)        # Local variable number
# def_op('STORE_FAST', 125)       # Local variable number
# haslocal.append(125)
e = [
    a for b in c
]

# def_op('DELETE_FAST', 126)      # Local variable number
def a():
    aa = 1
    del aa

# jrel_op('POP_JUMP_FORWARD_IF_NOT_NONE', 128)
if m.pi is None:
    pass

# jrel_op('POP_JUMP_FORWARD_IF_NONE', 129)
if not m.pi is None:
    pass

# def_op('RAISE_VARARGS', 130)    # Number of raise arguments (1, 2, or 3)
if m.pi > 3:
    raise

# def_op('GET_AWAITABLE', 131)
# def_op('MAKE_FUNCTION', 132)    # Flags
# def_op('BUILD_SLICE', 133)      # Number of items
async def runner():
    a = b[1:2]
    await inner()  # GET_AWAITABLE

# jrel_op('JUMP_BACKWARD_NO_INTERRUPT', 134) # Number of words to skip (backwards)
async def async_samples(async_iterable: Iterable[int]) -> None:
    async for _ in async_iterable:
        continue

# def_op('MAKE_CELL', 135)
# hasfree.append(135)
# def_op('LOAD_CLOSURE', 136)
# hasfree.append(136)
# def_op('LOAD_DEREF', 137)
# hasfree.append(137)
# def_op('STORE_DEREF', 138)
# hasfree.append(138)
# def_op('DELETE_DEREF', 139)
# hasfree.append(139)
def make_cell(val=None):
    x = val
    def closure():
        return x
    del x
    return closure.__closure__[0]

# jrel_op('JUMP_BACKWARD', 140)    # Number of words to skip (backwards)
for i in range(10):
    print()
    pass

# def_op('CALL_FUNCTION_EX', 142)  # Flags
call_ex(*(1, 2))  # CALL_FUNCTION_EX

###############################
# EXTENDED_ARG = 144          #
###############################

# def_op('EXTENDED_ARG', 144) 
def f(x):
    return x + 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21 + 22 + 23 + 24 + 25 + 26 + 27 + 28 + 29 + 30 + 31 + 32 + 33 + 34 + 35 + 36 + 37 + 38 + 39 + 40 + 41 + 42 + 43 + 44 + 45 + 46 + 47 + 48 + 49 + 50 + 51 + 52 + 53 + 54 + 55 + 56 + 57 + 58 + 59 + 60 + 61 + 62 + 63 + 64 + 65 + 66 + 67 + 68 + 69 + 70 + 71 + 72 + 73 + 74 + 75 + 76 + 77 + 78 + 79 + 80 + 81 + 82 + 83 + 84 + 85 + 86 + 87 + 88 + 89 + 90 + 91 + 92 + 93 + 94 + 95 + 96 + 97 + 98 + 99 + 100 + 101 + 102 + 103 + 104 + 105 + 106 + 107 + 108 + 109 + 110 + 111 + 112 + 113 + 114 + 115 + 116 + 117 + 118 + 119 + 120 + 121 + 122 + 123 + 124 + 125 + 126 + 127 + 128 + 129 + 130 + 131 + 132 + 133 + 134 + 135 + 136 + 137 + 138 + 139 + 140 + 141 + 142 + 143 + 144 + 145 + 146 + 147 + 148 + 149 + 150 + 151 + 152 + 153 + 154 + 155 + 156 + 157 + 158 + 159 + 160 + 161 + 162 + 163 + 164 + 165 + 166 + 167 + 168 + 169 + 170 + 171 + 172 + 173 + 174 + 175 + 176 + 177 + 178 + 179 + 180 + 181 + 182 + 183 + 184 + 185 + 186 + 187 + 188 + 189 + 190 + 191 + 192 + 193 + 194 + 195 + 196 + 197 + 198 + 199 + 200 + 201 + 202 + 203 + 204 + 205 + 206 + 207 + 208 + 209 + 210 + 211 + 212 + 213 + 214 + 215 + 216 + 217 + 218 + 219 + 220 + 221 + 222 + 223 + 224 + 225 + 226 + 227 + 228 + 229 + 230 + 231 + 232 + 233 + 234 + 235 + 236 + 237 + 238 + 239 + 240 + 241 + 242 + 243 + 244 + 245 + 246 + 247 + 248 + 249 + 250 + 251 + 252 + 253 + 254 + 255

# def_op('LIST_APPEND', 145)
[i for i in a]

# def_op('SET_ADD', 146)
{i for i in a}

# def_op('MAP_ADD', 147)
{i:i for i in a}

# def_op('LOAD_CLASSDEREF', 148)
# hasfree.append(148)
def foo():
    x = 3
    class Bar:
        print(x)


# def_op('COPY_FREE_VARS', 149)
def make_cell(val=None):
    x = val
    def closure():
        return x
    return closure.__closure__[0]

# def_op('RESUME', 151)   # This must be kept in sync with deepfreeze.py

# def_op('MATCH_CLASS', 152)
match Sample():
    case Sample():
        pass

# def_op('FORMAT_VALUE', 155)
# def_op('BUILD_STRING', 157)
f"value={1}"

# def_op('BUILD_CONST_KEY_MAP', 156)
{1:2, 2:3}

# name_op('LOAD_METHOD', 160)
fff.method(a)

# def_op('LIST_EXTEND', 162)
[*(1, 2, 3), 4]  # LIST_EXTEND

# def_op('SET_UPDATE', 163)
{*{1, 2}, 3}

# def_op('DICT_MERGE', 164)
dict(**dict1)

# def_op('DICT_UPDATE', 165)
{**{"a": 1}, "b": 2}

# def_op('PRECALL', 166)
# def_op('CALL', 171)
# def_op('KW_NAMES', 172)
# hasconst.append(172)
a(n=1)

# jrel_op('POP_JUMP_BACKWARD_IF_NOT_NONE', 173)
def backward():
    i = None
    while not i is None:
        i += 1

# jrel_op('POP_JUMP_BACKWARD_IF_NONE', 174)
def backward():
    i = None
    while i is None:
        i += 1

# jrel_op('POP_JUMP_BACKWARD_IF_FALSE', 175)
def backward():
    i = 0
    while not i < 1_000_000:
        i += 1

# jrel_op('POP_JUMP_BACKWARD_IF_TRUE', 176)
def backward():
    i = 0
    while i < 1_000_000:
        i += 1

# _nb_ops = [
#     ("NB_ADD", "+"),
#     ("NB_AND", "&"),
#     ("NB_FLOOR_DIVIDE", "//"),
#     ("NB_LSHIFT", "<<"),
#     ("NB_MATRIX_MULTIPLY", "@"),
#     ("NB_MULTIPLY", "*"),
#     ("NB_REMAINDER", "%"),
#     ("NB_OR", "|"),
#     ("NB_POWER", "**"),
#     ("NB_RSHIFT", ">>"),
#     ("NB_SUBTRACT", "-"),
#     ("NB_TRUE_DIVIDE", "/"),
#     ("NB_XOR", "^"),
#     ("NB_INPLACE_ADD", "+="),
#     ("NB_INPLACE_AND", "&="),
#     ("NB_INPLACE_FLOOR_DIVIDE", "//="),
#     ("NB_INPLACE_LSHIFT", "<<="),
#     ("NB_INPLACE_MATRIX_MULTIPLY", "@="),
#     ("NB_INPLACE_MULTIPLY", "*="),
#     ("NB_INPLACE_REMAINDER", "%="),
#     ("NB_INPLACE_OR", "|="),
#     ("NB_INPLACE_POWER", "**="),
#     ("NB_INPLACE_RSHIFT", ">>="),
#     ("NB_INPLACE_SUBTRACT", "-="),
#     ("NB_INPLACE_TRUE_DIVIDE", "/="),
#     ("NB_INPLACE_XOR", "^="),
# ]

# _specializations = {
#     "BINARY_OP": [
#         "BINARY_OP_ADAPTIVE",
#         "BINARY_OP_ADD_FLOAT",
#         "BINARY_OP_ADD_INT",
#         "BINARY_OP_ADD_UNICODE",
#         "BINARY_OP_INPLACE_ADD_UNICODE",
#         "BINARY_OP_MULTIPLY_FLOAT",
#         "BINARY_OP_MULTIPLY_INT",
#         "BINARY_OP_SUBTRACT_FLOAT",
#         "BINARY_OP_SUBTRACT_INT",
#     ],
#     "BINARY_SUBSCR": [
#         "BINARY_SUBSCR_ADAPTIVE",
#         "BINARY_SUBSCR_DICT",
#         "BINARY_SUBSCR_GETITEM",
#         "BINARY_SUBSCR_LIST_INT",
#         "BINARY_SUBSCR_TUPLE_INT",
#     ],
#     "CALL": [
#         "CALL_ADAPTIVE",
#         "CALL_PY_EXACT_ARGS",
#         "CALL_PY_WITH_DEFAULTS",
#     ],
#     "COMPARE_OP": [
#         "COMPARE_OP_ADAPTIVE",
#         "COMPARE_OP_FLOAT_JUMP",
#         "COMPARE_OP_INT_JUMP",
#         "COMPARE_OP_STR_JUMP",
#     ],
#     "EXTENDED_ARG": [
#         "EXTENDED_ARG_QUICK",
#     ],
#     "JUMP_BACKWARD": [
#         "JUMP_BACKWARD_QUICK",
#     ],
#     "LOAD_ATTR": [
#         "LOAD_ATTR_ADAPTIVE",
#         "LOAD_ATTR_INSTANCE_VALUE",
#         "LOAD_ATTR_MODULE",
#         "LOAD_ATTR_SLOT",
#         "LOAD_ATTR_WITH_HINT",
#     ],
#     "LOAD_CONST": [
#         "LOAD_CONST__LOAD_FAST",
#     ],
#     "LOAD_FAST": [
#         "LOAD_FAST__LOAD_CONST",
#         "LOAD_FAST__LOAD_FAST",
#     ],
#     "LOAD_GLOBAL": [
#         "LOAD_GLOBAL_ADAPTIVE",
#         "LOAD_GLOBAL_BUILTIN",
#         "LOAD_GLOBAL_MODULE",
#     ],
#     "LOAD_METHOD": [
#         "LOAD_METHOD_ADAPTIVE",
#         "LOAD_METHOD_CLASS",
#         "LOAD_METHOD_MODULE",
#         "LOAD_METHOD_NO_DICT",
#         "LOAD_METHOD_WITH_DICT",
#         "LOAD_METHOD_WITH_VALUES",
#     ],
#     "PRECALL": [
#         "PRECALL_ADAPTIVE",
#         "PRECALL_BOUND_METHOD",
#         "PRECALL_BUILTIN_CLASS",
#         "PRECALL_BUILTIN_FAST_WITH_KEYWORDS",
#         "PRECALL_METHOD_DESCRIPTOR_FAST_WITH_KEYWORDS",
#         "PRECALL_NO_KW_BUILTIN_FAST",
#         "PRECALL_NO_KW_BUILTIN_O",
#         "PRECALL_NO_KW_ISINSTANCE",
#         "PRECALL_NO_KW_LEN",
#         "PRECALL_NO_KW_LIST_APPEND",
#         "PRECALL_NO_KW_METHOD_DESCRIPTOR_FAST",
#         "PRECALL_NO_KW_METHOD_DESCRIPTOR_NOARGS",
#         "PRECALL_NO_KW_METHOD_DESCRIPTOR_O",
#         "PRECALL_NO_KW_STR_1",
#         "PRECALL_NO_KW_TUPLE_1",
#         "PRECALL_NO_KW_TYPE_1",
#         "PRECALL_PYFUNC",
#     ],
#     "RESUME": [
#         "RESUME_QUICK",
#     ],
#     "STORE_ATTR": [
#         "STORE_ATTR_ADAPTIVE",
#         "STORE_ATTR_INSTANCE_VALUE",
#         "STORE_ATTR_SLOT",
#         "STORE_ATTR_WITH_HINT",
#     ],
#     "STORE_FAST": [
#         "STORE_FAST__LOAD_FAST",
#         "STORE_FAST__STORE_FAST",
#     ],
#     "STORE_SUBSCR": [
#         "STORE_SUBSCR_ADAPTIVE",
#         "STORE_SUBSCR_DICT",
#         "STORE_SUBSCR_LIST_INT",
#     ],
#     "UNPACK_SEQUENCE": [
#         "UNPACK_SEQUENCE_ADAPTIVE",
#         "UNPACK_SEQUENCE_LIST",
#         "UNPACK_SEQUENCE_TUPLE",
#         "UNPACK_SEQUENCE_TWO_TUPLE",
#     ],
# }
# _specialized_instructions = [
#     opcode for family in _specializations.values() for opcode in family
# ]
# _specialization_stats = [
#     "success",
#     "failure",
#     "hit",
#     "deferred",
#     "miss",
#     "deopt",
# ]

# _cache_format = {
#     "LOAD_GLOBAL": {
#         "counter": 1,
#         "index": 1,
#         "module_keys_version": 2,
#         "builtin_keys_version": 1,
#     },
#     "BINARY_OP": {
#         "counter": 1,
#     },
#     "UNPACK_SEQUENCE": {
#         "counter": 1,
#     },
#     "COMPARE_OP": {
#         "counter": 1,
#         "mask": 1,
#     },
#     "BINARY_SUBSCR": {
#         "counter": 1,
#         "type_version": 2,
#         "func_version": 1,
#     },
#     "LOAD_ATTR": {
#         "counter": 1,
#         "version": 2,
#         "index": 1,
#     },
#     "STORE_ATTR": {
#         "counter": 1,
#         "version": 2,
#         "index": 1,
#     },
#     "LOAD_METHOD": {
#         "counter": 1,
#         "type_version": 2,
#         "dict_offset": 1,
#         "keys_version": 2,
#         "descr": 4,
#     },
#     "CALL": {
#         "counter": 1,
#         "func_version": 2,
#         "min_args": 1,
#     },
#     "PRECALL": {
#         "counter": 1,
#     },
#     "STORE_SUBSCR": {
#         "counter": 1,
#     },
# }

# _inline_cache_entries = [
#     sum(_cache_format.get(opname[opcode], {}).values()) for opcode in range(256)
# ]
