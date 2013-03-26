  use pib;
  drop table if exists NEWS;
  creat table NEWS(
      NEWS_ID int unsigned auto_increment,
      NEWS_DATE DATE not null,
      NEWS_TIMESTAMP datetime not null,
      NEWS_COUNTRY varchar(30) not null,
      NEWS_SORT varchar(30) not null,
      NEWS_INSTANCE varchar(30) not null,
      primary key(NEWS_ID)
      );
