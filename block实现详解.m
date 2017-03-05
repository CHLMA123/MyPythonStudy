

1. Block 实例

#include <stdio.h>  

int main(){    
 void (^blk)(void) = ^(){printf("This is a block.");};    
 blk();    
 return 0; 

}



#-------------------------------------------------------------------------------------------------------------------------

2. 使用clang 编译得到 .cpp 文件

struct __block_impl {
    void *isa;
    int Flags;
    int Reserved;
    void *FuncPtr;
};

struct __main_block_impl_0 {
    struct __block_impl impl;
    struct __main_block_desc_0* Desc;
    __main_block_impl_0(void *fp, struct __main_block_desc_0 *desc, int flags=0) {
        impl.isa = &_NSConcreteStackBlock;
        impl.Flags = flags;
        impl.FuncPtr = fp;
        Desc = desc;
    }
};

static void __main_block_func_0(struct __main_block_impl_0 *__cself) {
    printf("This is a block.");
}

static struct __main_block_desc_0 {
    size_t reserved;
    size_t Block_size;
} __main_block_desc_0_DATA = { 0, sizeof(struct __main_block_impl_0)};

int main(){
    void (*blk)(void) = (void (*)())&__main_block_impl_0((void *)__main_block_func_0
                        ,&__main_block_desc_0_DATA);
    ((void (*)(__block_impl *))((__block_impl *)blk)->FuncPtr)((__block_impl *)blk);
    return 0;
}

#-------------------------------------------------------------------------------------------------------------------------

3. 对main 文件 优化（去除一些强制转化）


int main(){

     void (*blk)(void) = &__main_block_impl_0(__main_block_func_0, &__main_block_desc_0_DATA);
     blk->FucPtr(blk)
    return 0;
}

解释过程：

		1. 可以看出来 block 是一个指向结构体的指针 &__main_block_impl_0（ ，，） 这个结构体实例是使用 该结构体的构造函数创建（c ++ 特性 ，结构体有构造函数）


				struct __main_block_impl_0 {
				struct __block_impl impl;
				struct __main_block_desc_0* Desc;
					__main_block_impl_0(void *fp, struct __main_block_desc_0 *desc, int flags=0) {
					    impl.isa = &_NSConcreteStackBlock;
					    impl.Flags = flags;
					    impl.FuncPtr = fp;
					    Desc = desc;
					}
				};


		2.  分析改结构体的传入的参数

		结构体有三个待传参数 1. void *fp (指向任意类型)
		                  2. struct __main_block_desc_0 (该结构体包含一个保留字段 reserved, 及Block_size)
		                  3. int flags (block 被copy 时执行的操作)

		在本例中只传了前两个值，第三个已经初始化等于 0 

                    第一个参数 __main_block_func_0   该参数是一个 方法名  实际就是指向 block 的方法
                    第二个参数 &__main_block_desc_0_DATA  该参数是 __main_block_desc_0 的一个实例 可以获取到block的内存大小


#-------------------------------------------------------------------------------------------------------------------------

   4. 从block 对应的结构体的构造函数 可以看出：当传入要实现的方法地址时，其内部有另外一个结构体的成员 指向改方法地址

   5. 从block 的调用中分析 是进行了 一系列的类型强制转化  将 blk （实际是__main_block_impl_0 类型的结构体） 强制转化成 __block_impl 型，然后调用其FucPtr 方法

        注： 此类转化为什么没有出问题是因为 结构体在实现时约定了一段内存空间，对每个成员有对应的内存布局，分配对应的大小
             查看这两个结构体可以看出 __main_block_impl_0 的第一个成员就是 __block_impl 所以 进行强制转化时，内存空间能够对应上，就不会引起值的变化，于是可以调用其对应的方法（详见 http://blog.csdn.net/kokodudu/article/details/13004951 ）
    
   该方法就是上述传入的方法 因为该方法有个参数 struct __main_block_impl_0 *__cself，所以调用的时候是 blk(blk);









