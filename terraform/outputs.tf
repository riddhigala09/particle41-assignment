output "load_balancer_dns" {
  value = aws_lb.simple_time_service_lb.dns_name
}