CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS name, b.size AS size FROM dogs AS a, sizes AS b WHERE a.height > b.min AND a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  -- SELECT d.name FROM dogs d, parents p, dogs dp WHERE p.child = d.name AND p.parent = dp.name ORDER BY dp.height DESC;
  SELECT p.child FROM parents AS p, dogs AS d WHERE p.parent = d.name ORDER BY height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS first, b.child AS second FROM parents a, parents b WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE siblings_have_same_size AS
  SELECT a.first AS first, a.second AS second, b.size AS size
  FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c
  WHERE a.first = b.name AND a.second = c.name AND b.size = c.size;

CREATE TABLE sentences AS
  SELECT first || ' and ' || second || ' are ' || size || ' siblings' FROM siblings_have_same_size;