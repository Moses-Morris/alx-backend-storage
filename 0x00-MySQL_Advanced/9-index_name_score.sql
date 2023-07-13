-- Create a =n index
CREATE INDEX idx_name_first_score on names(name(1), score);
