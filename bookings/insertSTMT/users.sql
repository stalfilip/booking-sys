use bookings

-- Innehåll för `users` tabell:

INSERT INTO `auth_user` (`username`, `first_name`, `last_name`, `email`, `password`, `date_joined`, `is_active`, `is_staff`, `is_superuser`)
VALUES
('annaL92', 'Anna', 'Larsson', 'anna.larsson@email.com', 'hashed_password_1', '2023-08-12 08:00:00', 1, 0, 0),
('erikJ78', 'Erik', 'Johansson', 'erik.johansson@email.com', 'hashed_password_2', '2023-08-10 09:15:00', 1, 0, 0),
('sofiaB87', 'Sofia', 'Bergman', 'sofia.bergman@email.com', 'hashed_password_3', '2023-07-30 14:45:00', 1, 0, 0),
('oscarN83', 'Oscar', 'Nilsson', 'oscar.nilsson@email.com', 'hashed_password_4', '2023-06-28 11:10:00', 1, 0, 0);

