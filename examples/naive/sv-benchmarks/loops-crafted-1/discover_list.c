int main(){
struct smp_target_obj tobj;
struct opts_t opts;
unsigned char * resp;
resp= (unsigned char *) malloc (sizeof (unsigned char));
int ret = do_discover_list( & tobj, __VERIFIER_nondet_int() , resp,  sizeof (resp),  & opts);
return 0;
}