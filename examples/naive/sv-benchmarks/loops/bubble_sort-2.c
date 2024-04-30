int main(void) 
{ struct list_head  const  *__cil_tmp1 ;
  struct list_head  const  *__cil_tmp2 ;

  {
  {
  gl_read();
  __cil_tmp1 = (struct list_head  const  *)(& gl_list);
  inspect(__cil_tmp1);
  gl_sort();
  __cil_tmp2 = (struct list_head  const  *)(& gl_list);
  inspect(__cil_tmp2);
  gl_destroy();
  }
  return (0);
}
}