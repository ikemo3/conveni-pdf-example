create table request (
    id int not null primary key,
    pdf_url varchar(1024) not null unique, -- ちゃんと一意制約をかける
    request_data json not null
);

create sequence request_id start 1;
