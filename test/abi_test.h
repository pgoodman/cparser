// 
// Tests for generating ABI library functions
// Anything with "my_callback"  or "my_varargs" should be excluded
// TODO: automate running this :)
//
int my_function(int a);
int my_varargs_function(int a, ...);
typedef void (*callback)();
struct bar {
  int x;
  float y;
  callback z;
};

union baz {
  struct bar b;
  void *q;
};

struct nocall {
  int a;
  int b;
  void *c;
  float *d;
  char arr[500];
};

int my_callback_function(int a, callback c);
int my_callback_function_array(int a, callback c[]);
int my_callback_function_array_fixed(int a, callback c[5]);
int my_callback_function_struct(int a, struct bar b);
int my_callback_function_struct_ptr(int a, struct bar *b);
int my_callback_function_union(int a, union baz b);
int my_callback_function_union_ptr(int a, union baz *b);
int my_callback_function_array_union(int a, union baz b[]);
int my_callback_function_array_union_ptr(int a, union baz *b[20]);
int my_callback_function_array_struct(int a, struct bar b[]);
int my_callback_function_array_struct_ptr(int a, struct bar *b[20]);


int no_callback_function_array_struct(int a, struct nocall b[]);
int no_callback_function_array_struct_ptr(int a, struct nocall *b[20]);
int no_callback_function_struct(int a, struct nocall b);
int no_callback_function_struct_ptr(int a, struct nocall *b);
