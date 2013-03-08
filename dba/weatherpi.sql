/*Database information for the raspberry pi bulletin board*/
use pib;

drop table if exists WEATHER;
create table WEATHER(
   WEATHER_ID int unsigned auto_increment,
   WEATHER_DATE DATE not null,
   WEATHER_TIMESTAMP datetime not null,
   WEATHER_CURRENT_TEMP int not null,
   WEATHER_CURRENT_STATUS varchar(30) not null,
   WEATHER_FORECAST_TEMP int not null,
   WEATHER_FORECAST_STATUS varchar(30) not null,
   primary key(WEATHER_ID)
);
