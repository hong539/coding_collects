--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
create table videos (
  vid_id int not null generated always as identity primary key
, vid_number text not null
);

create table tags (
  tag_id int not null generated always as identity primary key
, tag_name text not null
, unique(tag_name)
);

create table video_tags (
  vid_id int not null
, tag_id int not null
, unique(vid_id, tag_id)
);

--測試資料

insert into videos(vid_number)
values ('MEYD-844'), ('WAAA-293');

insert into tags (tag_name)
values ('熟女'),('人妻'),('巨乳'),('泳裝'),
       ('單體作品'),('高清'),('獨家'),('4K'),
       ('女教師'),('痴女'),('大屁股'),('中出');

insert into video_tags values
(1, 1), (1, 2), (1, 3), (1, 4),
(1, 5), (1, 6), (1, 7), (1, 8),
(2, 9), (2, 10),(2, 11), (2, 12),
(2, 3), (2, 1), (2, 8), (2, 7);