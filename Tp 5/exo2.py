from abc import ABC, abstractmethod

#product
class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

#products
class PDFReport(Report):
    def generate(self):
        pass

class ExcelReport(Report):
    def generate(self):
        pass

class WordReport(Report):
    def generate(self):
        pass

#factory
class ReportFactory:
    @staticmethod
    def create_report(report_type: str) -> Report:
        if report_type == "PDF":
            return PDFReport()
        elif report_type == "Excel":
            return ExcelReport()
        elif report_type == "Word":
            return WordReport()
        else:
            raise ValueError("Unknown report type")
