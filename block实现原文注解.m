
 参考 http://www.jianshu.com/p/ca6ac0ae93ad
 
#include <stdio.h>

int main(){
    
    void (^blk)(void) = ^(){printf("This is a block.");};
    blk();
    
    return 0;
}


// 该结构体作为 block 指向的结构体的 一个成员   
//    __block_impl保存block的类型isa（如&_NSConcreteStackBlock），标识（当block发生copy时，会用到），block的方法。

struct __block_impl {
    void *isa;    // 指向class 的指针
    int Flags;    // 当block 被copy 时应该执行的操作
    int Reserved;  // 保留字段
    void *FuncPtr;  // 指向block 内的函数实现
};


// block 指向的结构体
struct __main_block_impl_0 {    // c ++ 结构体

        struct __block_impl impl;
        struct __main_block_desc_0* Desc;

    // c ++ 结构体构造函数

        __main_block_impl_0(void *fp, struct __main_block_desc_0 *desc, int flags=0) {
            impl.isa = &_NSConcreteStackBlock;
            impl.Flags = flags;
            impl.FuncPtr = fp;
            Desc = desc;
        }


};

// block 的实现部分

static void __main_block_func_0(struct __main_block_impl_0 *__cself) {

    printf("This is a block.");
}



/*
    该结构体作为 block 指向的结构体的 一个成员
    __main_block_desc_0_DATA为__main_block_desc_0的一个结构体实例
    这个结构体，用来描述block的大小等信息。如果持有可修改的捕获变量时（即加__block），会增加两个函数（copy和dispose）

*/

static struct __main_block_desc_0 {
    size_t reserved;  // 保留字段 默认 0
    size_t Block_size;   // 用来保存block 所占内存的大小

} __main_block_desc_0_DATA = { 0, sizeof(struct __main_block_impl_0)};




int main(){
    // block 的转化

    void (*blk)(void) = (void (*)())&__main_block_impl_0((void *)__main_block_func_0,&__main_block_desc_0_DATA);


     // 去除干扰项  void (*blk)(void) = &__main_block_impl_0(__main_block_func_0, &__main_block_desc_0_DATA);
       
       /*
            block 是一个指向结构体的指针 （__main_block_impl_0），
            该行代码解释为：block 指向 __main_block_impl_0使用其构造函数 创建的一个结构体

       */


    ((void (*)(__block_impl *))((__block_impl *)blk)->FuncPtr)((__block_impl *)blk);

  /*
       去除转化代码后：
        blk->FucPtr(blk)

  */

    return 0;
}




