#include <stdio.h>
typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
typedef unsigned long    undefined7;
typedef unsigned long    undefined8;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef struct stat64 stat64, *Pstat64;

typedef ulong __dev_t;

typedef ulong __ino64_t;

typedef ulong __nlink_t;

typedef uint __mode_t;

typedef uint __uid_t;

typedef uint __gid_t;

typedef long __off_t;

typedef long __blksize_t;

typedef long __blkcnt64_t;

typedef struct timespec timespec, *Ptimespec;

typedef long __time_t;

struct timespec {
    __time_t tv_sec;
    long tv_nsec;
};

struct stat64 {
    __dev_t st_dev;
    __ino64_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt64_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    long __unused[3];
};

typedef struct stat stat, *Pstat;

typedef ulong __ino_t;

typedef long __blkcnt_t;

struct stat {
    __dev_t st_dev;
    __ino_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    long __unused[3];
};

typedef long __ssize_t;

typedef __ssize_t ssize_t;

typedef int __pid_t;

typedef long __clock_t;

typedef struct pollfd pollfd, *Ppollfd;

struct pollfd {
    int fd;
    short events;
    short revents;
};

typedef ulong nfds_t;

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

struct evp_pkey_ctx_st {
};

typedef uint pthread_key_t;

typedef union pthread_attr_t pthread_attr_t, *Ppthread_attr_t;

union pthread_attr_t {
    char __size[56];
    long __align;
};

typedef ulong pthread_t;

typedef struct astruct astruct, *Pastruct;

struct astruct {
    undefined field0_0x0;
    undefined field1_0x1;
    undefined field2_0x2;
    undefined field3_0x3;
    undefined field4_0x4;
    undefined field5_0x5;
    undefined field6_0x6;
    undefined field7_0x7;
    undefined field8_0x8;
    undefined field9_0x9;
    undefined field10_0xa;
    undefined field11_0xb;
    undefined field12_0xc;
    undefined field13_0xd;
    undefined field14_0xe;
    undefined field15_0xf;
    undefined field16_0x10;
    undefined field17_0x11;
    undefined field18_0x12;
    undefined field19_0x13;
    undefined field20_0x14;
    undefined field21_0x15;
    undefined field22_0x16;
    undefined field23_0x17;
    undefined field24_0x18;
    undefined field25_0x19;
    undefined field26_0x1a;
    undefined field27_0x1b;
    undefined field28_0x1c;
    undefined field29_0x1d;
    undefined field30_0x1e;
    undefined field31_0x1f;
    long charfield;
    long length;
};

typedef struct sigaltstack sigaltstack, *Psigaltstack;

typedef ulong size_t;

struct sigaltstack {
    void * ss_sp;
    int ss_flags;
    size_t ss_size;
};

typedef union sigval sigval, *Psigval;

union sigval {
    int sival_int;
    void * sival_ptr;
};

typedef struct siginfo siginfo, *Psiginfo;

typedef union _union_1438 _union_1438, *P_union_1438;

typedef struct _struct_1439 _struct_1439, *P_struct_1439;

typedef struct _struct_1440 _struct_1440, *P_struct_1440;

typedef struct _struct_1441 _struct_1441, *P_struct_1441;

typedef struct _struct_1442 _struct_1442, *P_struct_1442;

typedef struct _struct_1443 _struct_1443, *P_struct_1443;

typedef struct _struct_1444 _struct_1444, *P_struct_1444;

typedef union sigval sigval_t;

struct _struct_1444 {
    long si_band;
    int si_fd;
};

struct _struct_1443 {
    void * si_addr;
};

struct _struct_1442 {
    __pid_t si_pid;
    __uid_t si_uid;
    int si_status;
    __clock_t si_utime;
    __clock_t si_stime;
};

struct _struct_1441 {
    __pid_t si_pid;
    __uid_t si_uid;
    sigval_t si_sigval;
};

struct _struct_1440 {
    int si_tid;
    int si_overrun;
    sigval_t si_sigval;
};

struct _struct_1439 {
    __pid_t si_pid;
    __uid_t si_uid;
};

union _union_1438 {
    int _pad[28];
    struct _struct_1439 _kill;
    struct _struct_1440 _timer;
    struct _struct_1441 _rt;
    struct _struct_1442 _sigchld;
    struct _struct_1443 _sigfault;
    struct _struct_1444 _sigpoll;
};

struct siginfo {
    int si_signo;
    int si_errno;
    int si_code;
    union _union_1438 _sifields;
};

typedef struct siginfo siginfo_t;

typedef struct fs fs, *Pfs;

struct fs { // PlaceHolder Class Structure
};


typedef struct sigaction sigaction, *Psigaction;

typedef union _union_1454 _union_1454, *P_union_1454;

typedef struct __sigset_t __sigset_t, *P__sigset_t;

typedef void (* __sighandler_t)(int);

struct __sigset_t {
    ulong __val[16];
};

union _union_1454 {
    __sighandler_t sa_handler;
    void (* sa_sigaction)(int, siginfo_t *, void *);
};

struct sigaction {
    union _union_1454 __sigaction_handler;
    struct __sigset_t sa_mask;
    int sa_flags;
    void (* sa_restorer)(void);
};

typedef struct iovec iovec, *Piovec;

struct iovec {
    void * iov_base;
    size_t iov_len;
};

typedef enum Elf_ProgramHeaderType {
    PT_NULL=0,
    PT_LOAD=1,
    PT_DYNAMIC=2,
    PT_INTERP=3,
    PT_NOTE=4,
    PT_SHLIB=5,
    PT_PHDR=6,
    PT_TLS=7,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_STACK=1685382481,
    PT_GNU_RELRO=1685382482
} Elf_ProgramHeaderType;

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
};

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
    SHT_NULL=0,
    SHT_PROGBITS=1,
    SHT_SYMTAB=2,
    SHT_STRTAB=3,
    SHT_RELA=4,
    SHT_HASH=5,
    SHT_DYNAMIC=6,
    SHT_NOTE=7,
    SHT_NOBITS=8,
    SHT_REL=9,
    SHT_SHLIB=10,
    SHT_DYNSYM=11,
    SHT_INIT_ARRAY=14,
    SHT_FINI_ARRAY=15,
    SHT_PREINIT_ARRAY=16,
    SHT_GROUP=17,
    SHT_SYMTAB_SHNDX=18,
    SHT_ANDROID_REL=1610612737,
    SHT_ANDROID_RELA=1610612738,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_CHECKSUM=1879048184,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_syminfo=1879048188,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191
} Elf_SectionHeaderType;

struct Elf64_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType sh_type;
    qword sh_flags;
    qword sh_addr;
    qword sh_offset;
    qword sh_size;
    dword sh_link;
    dword sh_info;
    qword sh_addralign;
    qword sh_entsize;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

typedef enum Elf64_DynTag {
    DT_NULL=0,
    DT_NEEDED=1,
    DT_PLTRELSZ=2,
    DT_PLTGOT=3,
    DT_HASH=4,
    DT_STRTAB=5,
    DT_SYMTAB=6,
    DT_RELA=7,
    DT_RELASZ=8,
    DT_RELAENT=9,
    DT_STRSZ=10,
    DT_SYMENT=11,
    DT_INIT=12,
    DT_FINI=13,
    DT_SONAME=14,
    DT_RPATH=15,
    DT_SYMBOLIC=16,
    DT_REL=17,
    DT_RELSZ=18,
    DT_RELENT=19,
    DT_PLTREL=20,
    DT_DEBUG=21,
    DT_TEXTREL=22,
    DT_JMPREL=23,
    DT_BIND_NOW=24,
    DT_INIT_ARRAY=25,
    DT_FINI_ARRAY=26,
    DT_INIT_ARRAYSZ=27,
    DT_FINI_ARRAYSZ=28,
    DT_RUNPATH=29,
    DT_FLAGS=30,
    DT_PREINIT_ARRAY=32,
    DT_PREINIT_ARRAYSZ=33,
    DT_RELRSZ=35,
    DT_RELR=36,
    DT_RELRENT=37,
    DT_ANDROID_REL=1610612751,
    DT_ANDROID_RELSZ=1610612752,
    DT_ANDROID_RELA=1610612753,
    DT_ANDROID_RELASZ=1610612754,
    DT_ANDROID_RELR=1879040000,
    DT_ANDROID_RELRSZ=1879040001,
    DT_ANDROID_RELRENT=1879040003,
    DT_GNU_PRELINKED=1879047669,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_CHECKSUM=1879047672,
    DT_PLTPADSZ=1879047673,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_FEATURE_1=1879047676,
    DT_POSFLAG_1=1879047677,
    DT_SYMINSZ=1879047678,
    DT_SYMINENT=1879047679,
    DT_GNU_HASH=1879047925,
    DT_TLSDESC_PLT=1879047926,
    DT_TLSDESC_GOT=1879047927,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_LIBLIST=1879047929,
    DT_CONFIG=1879047930,
    DT_DEPAUDIT=1879047931,
    DT_AUDIT=1879047932,
    DT_PLTPAD=1879047933,
    DT_MOVETAB=1879047934,
    DT_SYMINFO=1879047935,
    DT_VERSYM=1879048176,
    DT_RELACOUNT=1879048185,
    DT_RELCOUNT=1879048186,
    DT_FLAGS_1=1879048187,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_AUXILIARY=2147483645,
    DT_FILTER=2147483647
} Elf64_DynTag;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct Gnu_BuildId Gnu_BuildId, *PGnu_BuildId;

struct Gnu_BuildId {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Build-id vendor name
    byte description[20]; // Build-id value
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

struct Elf64_Phdr {
    enum Elf_ProgramHeaderType p_type;
    dword p_flags;
    qword p_offset;
    qword p_vaddr;
    qword p_paddr;
    qword p_filesz;
    qword p_memsz;
    qword p_align;
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_osabi;
    byte e_ident_abiversion;
    byte e_ident_pad[7];
    word e_type;
    word e_machine;
    dword e_version;
    qword e_entry;
    qword e_phoff;
    qword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};

void main(void)

{
  int iVar1;
  int iVar2;
  uint *puVar3;
  byte bVar4;
  byte bVar5;
  char cVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  uint uVar10;
  uint uVar11;
  uint uVar12;
  uint uVar13;
  uint uVar14;
  undefined **ppuVar15;
  uint uVar16;
  uint uVar17;
  uint uVar18;
  uint uVar19;
  uint uVar20;
  uint uVar21;
  uint uVar22;
  uint uVar23;
  uint uVar24;
  uint uVar25;
  uint uVar26;
  uint uVar27;
  uint uVar28;
  uint uVar29;
  uint uVar30;
  uint uVar31;
  uint uVar32;
  uint uVar33;
  uint uVar34;
  uint uVar35;
  uint uVar36;
  uint uVar37;
  uint uVar38;
  long counter;
  uint uVar39;
  uint uVar40;
  uint uVar41;
  uint uVar42;
  uint uVar43;
  uint uVar44;
  int iVar45;
  uint uVar46;
  uint uVar47;
  uint uVar48;
  uint uVar49;
  uint uVar50;
  uint uVar51;
  astruct **local_238;
  undefined4 uStack560;
  undefined4 uStack556;
  undefined **local_228;
  undefined8 uStack544;
  char *local_218;
  undefined8 local_210;
  int local_200;
  int local_1fc;
  int local_1f8;
  int local_1f4;
  int local_1f0;
  int local_1ec;
  int local_1e8;
  int local_1e4;
  int local_1e0;
  int local_1dc;
  int local_1d8;
  int local_1d4;
  int local_1d0;
  int local_1cc;
  int local_1c8;
  int local_1c4;
  int local_1c0;
  int local_1bc;
  int local_1b8;
  int local_1b4;
  int local_1b0;
  int local_1ac;
  int local_1a8;
  int local_1a4;
  int local_1a0;
  int local_19c;
  int local_198;
  int local_194;
  long local_190;
  astruct *argstart_;
  ulong argcount;
  astruct *local_178;
  char *char_at_0x20;
  long local_168;
  ulong local_160;
  ulong local_158;
  ulong local_150;
  ulong local_148;
  ulong local_140;
  ulong local_138;
  ulong local_130;
  ulong local_128;
  ulong local_120;
  ulong local_118;
  ulong local_110;
  ulong local_108;
  ulong local_100;
  ulong local_f8;
  ulong local_f0;
  ulong local_e8;
  ulong local_e0;
  ulong local_d8;
  ulong local_d0;
  ulong local_c8;
  ulong local_c0;
  ulong local_b8;
  ulong local_b0;
  ulong local_a8;
  ulong local_a0;
  ulong local_98;
  ulong local_90;
  ulong local_88;
  ulong local_80;
  ulong local_78;
  ulong local_70;
  ulong local_68;
  ulong local_60;
  astruct *local_58;
  astruct **local_50;
  undefined8 uStack72;
  undefined4 local_40;
  undefined4 uStack60;
  undefined4 uStack56;
  undefined4 uStack52;

int ar[13] = {0xDB9BDB0D,     0xFDE8FB2,    0xCA379BBB,    0xACAC25B8,
0x464FD6E5,    0x52584811,    0xE27DC301,    0x55E48BF8,
0xB984194,    0xB23AADE7,    0x1B9D2631,    0xFDB5C4CC,
0xA3D6A5B3};

  for(int i = 0; i < 13; i++){
  for(unsigned char c1 = 0; c1 < 0xff; c1++){
    for(unsigned char c2 = 0; c2 < 0xff; c2++){

      bVar4 = c1;
      bVar5 = c2;
      cVar6 = bVar5 * bVar4;
      if (cVar6 == '\0') {
        uVar42 = 0x70e11488;
      }
      else {
        uVar28 = (uint)bVar5 * 0x100;
        uVar8 = (uint)bVar4;
        uVar41 = (uint)(bVar4* 0x10000) + bVar5 * 0x100  + bVar5 ;
        uVar43 = uVar8 * 0x1000000;
        uVar7 = (uint)bVar5;
        uVar42 = uVar43 + uVar7 * 0x10000;
        iVar45 = uVar42 + uVar28;
        uVar38 = uVar7 * 0x10000 | uVar7 << 0x18;
        iVar1 = uVar38 + uVar28;
        uVar48 = uVar7 << 0x18 | uVar8 << 0x10;
        iVar2 = uVar48 + uVar28;
        uVar39 = uVar8 << 8;
        uVar38 = uVar38 | uVar39;
        uVar44 = uVar8 << 0x10 | uVar43;
        uVar28 = uVar28 | uVar44;
        uVar44 = uVar44 | uVar39;
        uVar48 = uVar48 | uVar39;
        uVar39 = uVar39 | uVar42;
        uVar16 = uVar43 + uVar41 + 0x4dae395b;
        local_60 = (ulong)uVar16;
        uVar8 = uVar43 + 0x865aa9f3 + uVar41;
        local_68 = (ulong)uVar8;
        local_194 = uVar43 + 0x3654265e + uVar41;
        uVar41 = uVar43 + 0x52e763dc + uVar41;
        local_70 = (ulong)uVar41;
        local_78 = (ulong)(iVar45 + (uint)bVar4);
        uVar17 = bVar4 + 0x22caf51b + iVar45;
        local_80 = (ulong)uVar17;
        local_198 = bVar4 + 0x17d2b95f + iVar45;
        local_19c = bVar4 + 0x4c3c75d + iVar45;
        local_88 = (ulong)(iVar1 + (uint)bVar4);
        local_1a0 = bVar4 + 0x47933969 + iVar1;
        local_1a4 = bVar4 + 0xaf883dec + iVar1;
        uVar18 = bVar4 + 0x90edeca5 + iVar1;
        local_90 = (ulong)uVar18;
        uVar19 = bVar4 + 0x9ee61754 + iVar1;
        local_98 = (ulong)uVar19;
        uVar20 = bVar4 + 0xae4dfffa + iVar1;
        local_a0 = (ulong)uVar20;
        uVar21 = bVar4 + 0x337e4d32 + iVar1;
        local_a8 = (ulong)uVar21;
        local_1a8 = bVar4 + 0x6e5af54 + iVar1;
        local_1ac = bVar4 + 0xcea4cd09 + iVar1;
        uVar22 = bVar4 + 0x7d5c4787 + iVar1;
        local_b0 = (ulong)uVar22;
        uVar23 = bVar4 + 0xd6635932 + iVar1;
        local_b8 = (ulong)uVar23;
        uVar24 = bVar4 + 0xe6893e3e + iVar1;
        local_c0 = (ulong)uVar24;
        local_1b0 = uVar28 + bVar4;
        local_1b4 = bVar4 + 0x727bc379 + uVar28;
        uVar25 = bVar4 + 0x8eb2728d + uVar28;
        local_c8 = (ulong)uVar25;
        uVar26 = bVar4 + 0xe9f0bb6c + uVar28;
        local_d0 = (ulong)uVar26;
        local_1b8 = bVar4 + 0x3065d239 + uVar28;
        local_1bc = bVar4 + 0x5cce65ea + uVar28;
        uVar27 = bVar4 + 0xc3cd9ad8 + uVar28;
        local_d8 = (ulong)uVar27;
        uVar28 = bVar4 + 0x68f629d8 + uVar28;
        local_e0 = (ulong)uVar28;
        local_e8 = (ulong)(iVar2 + (uint)bVar4);
        local_1c0 = bVar4 + 0xd16cc010 + iVar2;
        uVar29 = bVar4 + 0x60541226 + iVar2;
        local_f0 = (ulong)uVar29;
        uVar30 = bVar4 + 0x6ea16787 + iVar2;
        local_f8 = (ulong)uVar30;
        local_1c4 = bVar4 + 0x957bcab2 + iVar2;
        local_1c8 = bVar4 + 0x13205a9 + iVar2;
        uVar31 = bVar4 + 0x3e11613b + iVar2;
        local_100 = (ulong)uVar31;
        uVar32 = bVar4 + 0xb1d75427 + iVar2;
        local_108 = (ulong)uVar32;
        local_1cc = bVar4 + 0xc4525dba + uVar38;
        local_1d0 = bVar4 + 0x29ed3c63 + uVar38;
        local_1d4 = bVar4 + 0xadc8c656 + uVar38;
        uVar33 = bVar4 + 0xdb3b14e4 + uVar38;
        local_110 = (ulong)uVar33;
        local_1d8 = bVar4 + 0x1429a203 + uVar38;
        local_1dc = bVar4 + 0x2b8176d5 + uVar38;
        uVar34 = bVar4 + 0x1ca719d8 + uVar38;
        local_118 = (ulong)uVar34;
        uVar43 = bVar4 + 0xf8bdcac8 + uVar38;
        local_120 = (ulong)uVar43;
        uVar9 = bVar5 + 0x9d52d37f + uVar38;
        local_128 = (ulong)uVar9;
        local_1e0 = bVar5 + 0x50e63ca3 + uVar38;
        uVar10 = bVar5 + uVar38 + 0x305f8997;
        local_130 = (ulong)uVar10;
        local_1e4 = bVar5 + uVar48 + -0x68cc0348;
        uVar11 = bVar5 + 0x18c535c3 + uVar48;
        local_138 = (ulong)uVar11;
        local_1e8 = bVar5 + 0x9c305131 + uVar48;
        uVar48 = bVar5 + 0x4111b65a + uVar48;
        local_140 = (ulong)uVar48;
        local_1ec = bVar5 + 0xa64a2af5 + uVar39;
        local_1f0 = bVar5 + 0x70ae1ee0 + uVar39;
        local_1f4 = bVar5 + 0xe0c0abfd + uVar39;
        uVar12 = bVar5 + 0x75d8eb96 + uVar39;
        local_148 = (ulong)uVar12;
        local_1f8 = bVar5 + 0xe24ebc08 + uVar39;
        local_1fc = bVar5 + 0x7fe792d6 + uVar39;
        uVar13 = bVar5 + 0xb9d772ff + uVar39;
        local_150 = (ulong)uVar13;
        uVar39 = bVar5 + 0xa1578c9c + uVar39;
        local_158 = (ulong)uVar39;
        local_200 = bVar5 + 0x4b3a21ca + uVar44;
        uVar14 = bVar5 + 0x6c828dc8 + uVar44;
        local_160 = (ulong)uVar14;
        uVar47 = 0xb484dcdc;
        uVar51 = 0x3be4d5bf;
        uVar42 = 0x7e5f221f;
        uVar37 = 0x81de3ff4;
        do {
          uVar35 = iVar45 + (uint)bVar4 + (uVar42 & uVar51) + uVar37 + (~uVar42 & uVar47) +
                   0x3bcb2ec4;
          uVar36 = (uVar35 * 0x80 | uVar35 >> 0x19) + uVar42;
          uVar35 = (~uVar36 & uVar51) + uVar47 + iVar1 + (uint)bVar4 + (uVar36 & uVar42) +
                   0x97dc7dad;
          uVar40 = (uVar35 * 0x1000 | uVar35 >> 0x14) + uVar36;
          uVar35 = (uVar40 & uVar36) + (~uVar40 & uVar42) + iVar2 + (uint)bVar4 + uVar51 +
                   0x7fbf88d8;
          uVar46 = (uVar35 * 0x20000 | uVar35 >> 0xf) + uVar40;
          uVar35 = (~uVar46 & uVar36) + uVar42 + (uVar38 | uVar7) + (uVar46 & uVar40) + 0x577f129e;
          uVar35 = (uVar35 * 0x400000 | uVar35 >> 10) + uVar46;
          uVar36 = uVar36 + local_1b0 + (~uVar35 & uVar40) + (uVar35 & uVar46) + 0x91d9bb31;
          uVar36 = (uVar36 * 0x80 | uVar36 >> 0x19) + uVar35;
          uVar40 = uVar40 + local_1a0 + (~uVar36 & uVar46) + (uVar36 & uVar35);
          uVar40 = (uVar40 * 0x1000 | uVar40 >> 0x14) + uVar36;
          uVar46 = uVar46 + local_1cc + (~uVar40 & uVar35) + (uVar40 & uVar36);
          uVar46 = (uVar46 * 0x20000 | uVar46 >> 0xf) + uVar40;
          uVar35 = uVar35 + local_1a4 + (~uVar46 & uVar36) + (uVar46 & uVar40);
          uVar35 = (uVar35 * 0x400000 | uVar35 >> 10) + uVar46;
          uVar36 = uVar36 + local_1c0 + (~uVar35 & uVar40) + (uVar35 & uVar46);
          uVar36 = (uVar36 * 0x80 | uVar36 >> 0x19) + uVar35;
          uVar40 = uVar40 + local_200 + (~uVar36 & uVar46) + (uVar36 & uVar35);
          uVar40 = (uVar40 * 0x1000 | uVar40 >> 0x14) + uVar36;
          uVar46 = uVar46 + local_1e4 + (~uVar40 & uVar35) + (uVar40 & uVar36);
          uVar46 = (uVar46 * 0x20000 | uVar46 >> 0xf) + uVar40;
          uVar35 = uVar35 + local_1ec + (~uVar46 & uVar36) + (uVar46 & uVar40);
          uVar35 = (uVar35 * 0x400000 | uVar35 >> 10) + uVar46;
          uVar36 = uVar36 + local_1d0 + (~uVar35 & uVar40) + (uVar35 & uVar46);
          uVar36 = (uVar36 * 0x80 | uVar36 >> 0x19) + uVar35;
          uVar40 = uVar40 + local_1f0 + (~uVar36 & uVar46) + (uVar36 & uVar35);
          uVar40 = (uVar40 * 0x1000 | uVar40 >> 0x14) + uVar36;
          uVar46 = uVar46 + local_1b4 + (uVar35 & ~uVar40) + (uVar40 & uVar36);
          uVar46 = (uVar46 * 0x20000 | uVar46 >> 0xf) + uVar40;
          uVar35 = (uVar36 & ~uVar46) + uVar16 + uVar35 + (uVar46 & uVar40);
          uVar35 = (uVar35 * 0x400000 | uVar35 >> 10) + uVar46;
          uVar36 = (~uVar40 & uVar46) + uVar18 + uVar36 + (uVar35 & uVar40);
          uVar49 = (uVar36 * 0x20 | uVar36 >> 0x1b) + uVar35;
          uVar36 = uVar40 + local_1d4 + (~uVar46 & uVar35) + (uVar49 & uVar46);
          uVar36 = (uVar36 * 0x200 | uVar36 >> 0x17) + uVar49;
          uVar40 = uVar46 + local_1f4 + (~uVar35 & uVar49) + (uVar36 & uVar35);
          uVar40 = (uVar40 * 0x4000 | uVar40 >> 0x12) + uVar36;
          uVar35 = (~uVar49 & uVar36) + uVar17 + uVar35 + (uVar40 & uVar49);
          uVar50 = (uVar35 * 0x100000 | uVar35 >> 0xc) + uVar40;
          uVar35 = (~uVar36 & uVar40) + uVar19 + uVar49 + (uVar50 & uVar36);
          uVar35 = (uVar35 * 0x20 | uVar35 >> 0x1b) + uVar50;
          uVar36 = (~uVar40 & uVar50) + uVar11 + uVar36 + (uVar35 & uVar40);
          uVar46 = (uVar36 * 0x200 | uVar36 >> 0x17) + uVar35;
          uVar36 = (~uVar50 & uVar35) + uVar8 + uVar40 + (uVar46 & uVar50);
          uVar49 = (uVar36 * 0x4000 | uVar36 >> 0x12) + uVar46;
          uVar36 = (~uVar35 & uVar46) + uVar25 + uVar50 + (uVar49 & uVar35);
          uVar36 = (uVar36 * 0x100000 | uVar36 >> 0xc) + uVar49;
          uVar35 = (~uVar46 & uVar49) + uVar14 + uVar35 + (uVar36 & uVar46);
          uVar40 = (uVar35 * 0x20 | uVar35 >> 0x1b) + uVar36;
          uVar35 = (~uVar49 & uVar36) + uVar26 + uVar46 + (uVar40 & uVar49);
          uVar50 = (uVar35 * 0x200 | uVar35 >> 0x17) + uVar40;
          uVar35 = (~uVar36 & uVar40) + uVar9 + uVar49 + (uVar50 & uVar36);
          uVar35 = (uVar35 * 0x4000 | uVar35 >> 0x12) + uVar50;
          uVar36 = (~uVar40 & uVar50) + uVar29 + uVar36 + (uVar35 & uVar40);
          uVar46 = (uVar36 * 0x100000 | uVar36 >> 0xc) + uVar35;
          uVar36 = (~uVar50 & uVar35) + uVar12 + uVar40 + (uVar46 & uVar50);
          uVar49 = (uVar36 * 0x20 | uVar36 >> 0x1b) + uVar46;
          uVar36 = (~uVar35 & uVar46) + uVar30 + uVar50 + (uVar49 & uVar35);
          uVar36 = (uVar36 * 0x200 | uVar36 >> 0x17) + uVar49;
          uVar35 = (~uVar46 & uVar49) + uVar20 + uVar35 + (uVar36 & uVar46);
          uVar40 = (uVar35 * 0x4000 | uVar35 >> 0x12) + uVar36;
          uVar35 = (~uVar49 & uVar36) + uVar33 + uVar46 + (uVar40 & uVar49);
          uVar46 = (uVar35 * 0x100000 | uVar35 >> 0xc) + uVar40;
          uVar35 = (uVar46 ^ uVar40 ^ uVar36) + uVar21 + uVar49;
          uVar35 = (uVar35 * 0x10 | uVar35 >> 0x1c) + uVar46;
          uVar36 = uVar36 + local_1c4 + (uVar46 ^ uVar40 ^ uVar35);
          uVar36 = (uVar36 * 0x800 | uVar36 >> 0x15) + uVar35;
          uVar40 = uVar40 + local_1f8 + (uVar36 ^ uVar35 ^ uVar46);
          uVar40 = (uVar40 * 0x10000 | uVar40 >> 0x10) + uVar36;
          uVar46 = uVar46 + local_1b8 + (uVar36 ^ uVar35 ^ uVar40);
          uVar46 = (uVar46 * 0x800000 | uVar46 >> 9) + uVar40;
          uVar35 = uVar35 + local_1a8 + (uVar46 ^ uVar40 ^ uVar36);
          uVar35 = (uVar35 * 0x10 | uVar35 >> 0x1c) + uVar46;
          uVar36 = uVar36 + local_1bc + (uVar46 ^ uVar40 ^ uVar35);
          uVar36 = (uVar36 * 0x800 | uVar36 >> 0x15) + uVar35;
          uVar40 = uVar40 + local_1ac + (uVar36 ^ uVar35 ^ uVar46);
          uVar40 = (uVar40 * 0x10000 | uVar40 >> 0x10) + uVar36;
          uVar46 = uVar46 + local_1e8 + (uVar36 ^ uVar35 ^ uVar40);
          uVar46 = (uVar46 * 0x800000 | uVar46 >> 9) + uVar40;
          uVar35 = uVar35 + local_1fc + (uVar46 ^ uVar40 ^ uVar36);
          uVar35 = (uVar35 * 0x10 | uVar35 >> 0x1c) + uVar46;
          uVar36 = uVar36 + local_198 + (uVar46 ^ uVar40 ^ uVar35);
          uVar36 = (uVar36 * 0x800 | uVar36 >> 0x15) + uVar35;
          uVar40 = uVar40 + local_1e0 + (uVar35 ^ uVar46 ^ uVar36);
          uVar40 = (uVar40 * 0x10000 | uVar40 >> 0x10) + uVar36;
          uVar46 = uVar46 + local_1d8 + (uVar36 ^ uVar35 ^ uVar40);
          uVar46 = (uVar46 * 0x800000 | uVar46 >> 9) + uVar40;
          uVar35 = uVar35 + bVar5 + 0x9edfe0eb + uVar44 + (uVar40 ^ uVar36 ^ uVar46);
          uVar35 = (uVar35 * 0x10 | uVar35 >> 0x1c) + uVar46;
          uVar36 = uVar36 + local_1dc + (uVar46 ^ uVar40 ^ uVar35);
          uVar36 = (uVar36 * 0x800 | uVar36 >> 0x15) + uVar35;
          uVar40 = uVar40 + local_194 + (uVar35 ^ uVar46 ^ uVar36);
          uVar40 = (uVar40 * 0x10000 | uVar40 >> 0x10) + uVar36;
          uVar46 = uVar46 + local_1c8 + (uVar36 ^ uVar35 ^ uVar40);
          uVar49 = (uVar46 * 0x800000 | uVar46 >> 9) + uVar40;
          uVar35 = uVar35 + local_19c + ((~uVar36 | uVar49) ^ uVar40);
          uVar35 = (uVar35 * 0x40 | uVar35 >> 0x1a) + uVar49;
          uVar36 = ((~uVar40 | uVar35) ^ uVar49) + uVar22 + uVar36;
          uVar46 = (uVar36 * 0x400 | uVar36 >> 0x16) + uVar35;
          uVar36 = ((~uVar49 | uVar46) ^ uVar35) + uVar27 + uVar40;
          uVar50 = (uVar36 * 0x8000 | uVar36 >> 0x11) + uVar46;
          uVar36 = ((~uVar35 | uVar50) ^ uVar46) + uVar23 + uVar49;
          uVar36 = (uVar36 * 0x200000 | uVar36 >> 0xb) + uVar50;
          uVar35 = ((~uVar46 | uVar36) ^ uVar50) + uVar34 + uVar35;
          uVar40 = (uVar35 * 0x40 | uVar35 >> 0x1a) + uVar36;
          uVar35 = ((~uVar50 | uVar40) ^ uVar36) + uVar10 + uVar46;
          uVar49 = (uVar35 * 0x400 | uVar35 >> 0x16) + uVar40;
          uVar35 = ((~uVar36 | uVar49) ^ uVar40) + uVar48 + uVar50;
          uVar35 = (uVar35 * 0x8000 | uVar35 >> 0x11) + uVar49;
          uVar36 = ((~uVar40 | uVar35) ^ uVar49) + uVar24 + uVar36;
          uVar46 = (uVar36 * 0x200000 | uVar36 >> 0xb) + uVar35;
          uVar36 = ((~uVar49 | uVar46) ^ uVar35) + uVar31 + uVar40;
          uVar40 = (uVar36 * 0x40 | uVar36 >> 0x1a) + uVar46;
          uVar36 = ((~uVar35 | uVar40) ^ uVar46) + uVar41 + uVar49;
          uVar36 = (uVar36 * 0x400 | uVar36 >> 0x16) + uVar40;
          uVar35 = ((~uVar46 | uVar36) ^ uVar40) + uVar43 + uVar35;
          uVar49 = (uVar35 * 0x8000 | uVar35 >> 0x11) + uVar36;
          uVar35 = ((~uVar40 | uVar49) ^ uVar36) + uVar13 + uVar46;
          uVar46 = (uVar35 * 0x200000 | uVar35 >> 0xb) + uVar49;
          uVar35 = ((~uVar36 | uVar46) ^ uVar49) + uVar28 + uVar40;
          uVar40 = (uVar35 * 0x40 | uVar35 >> 0x1a) + uVar46;
          uVar35 = ((~uVar49 | uVar40) ^ uVar46) + uVar39 + uVar36;
          uVar36 = (uVar35 * 0x400 | uVar35 >> 0x16) + uVar40;
          uVar35 = ((~uVar46 | uVar36) ^ uVar40) + uVar32 + uVar49;
          uVar49 = (uVar35 * 0x8000 | uVar35 >> 0x11) + uVar36;
          uVar35 = ((~uVar40 | uVar49) ^ uVar36) + bVar5 + 0x53d1a3b2 + uVar44 + uVar46;
          uVar37 = uVar40 + uVar37;
          uVar42 = uVar42 + uVar49 + (uVar35 * 0x200000 | uVar35 >> 0xb);
          uVar51 = uVar49 + uVar51;
          uVar47 = uVar36 + uVar47;
          cVar6 = cVar6 + -1;
        } while (cVar6 != '\0');
        uVar42 = uVar47 ^ uVar37 ^ uVar51 ^ uVar42;
        
        local_168 = counter;
      }
      if(uVar42 == ar[i]){
        printf("%c %c %08X\n", bVar4, bVar5, uVar42);
      }
    }
  }
  }
}
