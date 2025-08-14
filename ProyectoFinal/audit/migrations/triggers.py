from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', 'tables'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TRIGGER trg_employee_audit
            AFTER UPDATE ON reservations_employee
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'reservations_employee',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'salary', OLD.salary,
                        'start_date', OLD.start_date,
                        'role_id', OLD.role_id
                    ),
                    json_object(
                        'salary', NEW.salary,
                        'start_date', NEW.start_date,
                        'role_id', NEW.role_id
                    ),
                    datetime('now'),
                    'Employee data updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_employee_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_employee_delete_audit
            BEFORE DELETE ON reservations_employee
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, timestamp, description
                ) VALUES (
                    'reservations_employee',
                    'DELETE',
                    OLD.id,
                    json_object(
                        'person_id', OLD.person_id,
                        'role_id', OLD.role_id,
                        'salary', OLD.salary,
                        'start_date', OLD.start_date,
                        'hotel_id', OLD.hotel_id
                    ),
                    datetime('now'),
                    'Employee deleted'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_employee_delete_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_room_audit
            AFTER UPDATE ON rooms_room
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'rooms_room',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'price', OLD.price,
                        'beds_qty', OLD.beds_qty,
                        'room_category_id', OLD.room_category_id
                    ),
                    json_object(
                        'price', NEW.price,
                        'beds_qty', NEW.beds_qty,
                        'room_category_id', NEW.room_category_id
                    ),
                    datetime('now'),
                    'Room data updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_room_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_reservation_insert_audit
            AFTER INSERT ON reservations_roomreservation
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, new_values, timestamp, description
                ) VALUES (
                    'reservations_roomreservation',
                    'INSERT',
                    NEW.id,
                    json_object(
                        'room_id', NEW.room_id,
                        'customer_id', NEW.customer_id,
                        'check_in_date', NEW.check_in_date,
                        'check_out_date', NEW.check_out_date,
                        'price', NEW.price
                    ),
                    datetime('now'),
                    'Reservation created'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_reservation_insert_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_reservation_update_audit
            AFTER UPDATE ON reservations_roomreservation
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'reservations_roomreservation',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'check_in_date', OLD.check_in_date,
                        'check_out_date', OLD.check_out_date,
                        'price', OLD.price
                    ),
                    json_object(
                        'check_in_date', NEW.check_in_date,
                        'check_out_date', NEW.check_out_date,
                        'price', NEW.price
                    ),
                    datetime('now'),
                    'Reservation updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_reservation_update_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_reservation_delete_audit
            BEFORE DELETE ON reservations_roomreservation
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, timestamp, description
                ) VALUES (
                    'reservations_roomreservation',
                    'DELETE',
                    OLD.id,
                    json_object(
                        'room_id', OLD.room_id,
                        'customer_id', OLD.customer_id,
                        'check_in_date', OLD.check_in_date,
                        'check_out_date', OLD.check_out_date,
                        'price', OLD.price
                    ),
                    datetime('now'),
                    'Reservation deleted'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_reservation_delete_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_activity_audit
            AFTER UPDATE ON reservations_activity
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'reservations_activity',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'price', OLD.price,
                        'activity_category_id', OLD.activity_category_id
                    ),
                    json_object(
                        'price', NEW.price,
                        'activity_category_id', NEW.activity_category_id
                    ),
                    datetime('now'),
                    'Activity updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_activity_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_room_status_audit
            AFTER INSERT ON rooms_roomstatus
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, new_values, timestamp, description
                ) VALUES (
                    'rooms_roomstatus',
                    'INSERT',
                    NEW.id,
                    json_object(
                        'room_id', NEW.room_id,
                        'status_id', NEW.status_id,
                        'comment', NEW.comment
                    ),
                    datetime('now'),
                    'Room status updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_room_status_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_supplier_audit
            AFTER UPDATE ON reservations_supplier
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'reservations_supplier',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'name', OLD.name,
                        'contact_person_name', OLD.contact_person_name,
                        'phone_number', OLD.phone_number,
                        'location', OLD.location
                    ),
                    json_object(
                        'name', NEW.name,
                        'contact_person_name', NEW.contact_person_name,
                        'phone_number', NEW.phone_number,
                        'location', NEW.location
                    ),
                    datetime('now'),
                    'Supplier updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_supplier_audit;"
        ),
        

        migrations.RunSQL(
            """
            CREATE TRIGGER trg_supply_audit
            AFTER UPDATE ON reservations_supply
            FOR EACH ROW
            BEGIN
                INSERT INTO audit_log (
                    table_name, action, record_id, old_values, new_values, timestamp, description
                ) VALUES (
                    'reservations_supply',
                    'UPDATE',
                    NEW.id,
                    json_object(
                        'supply_name', OLD.supply_name,
                        'total_price', OLD.total_price,
                        'city', OLD.city
                    ),
                    json_object(
                        'supply_name', NEW.supply_name,
                        'total_price', NEW.total_price,
                        'city', NEW.city
                    ),
                    datetime('now'),
                    'Supply updated'
                );
            END;
            """,
            reverse_sql="DROP TRIGGER IF EXISTS trg_supply_audit;"
        ),
    ]
