--src: https://hackmd.io/@pgsql-tw/rJSOHh8zT
select t.tag_name
  from videos_array va
  cross join unnest(va.vid_tags) as tag_id
  join tags t
 using (tag_id)
 where va.vid_number = 'MEYD-844';