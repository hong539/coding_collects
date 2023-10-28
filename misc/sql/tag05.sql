--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
create table videos_array (
  vid_id int not null primary key
, vid_number text not null
, vid_tags int[]
);

insert into videos_array
select v.vid_id, vid_number, array_agg(tag_id)
  from videos v
  join video_tags
  using (vid_id)
  group by v.vid_id, vid_number;
  
select *
  from videos_array;