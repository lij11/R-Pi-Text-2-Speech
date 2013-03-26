   use pib;
  
   drop table if exists JOKES;
   creat table JOKES(
       JOKES_ID int unsigned auto_increment,
       JOKES_SORT varchar(30) not null,
       primary key(JOKES_ID)
       );
